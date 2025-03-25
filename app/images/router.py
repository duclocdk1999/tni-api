import os
from typing import List
from fastapi import APIRouter, Depends, UploadFile
from sqlmodel import Session

from app.config import STATIC_DIR
from app.images.crud import get_images, get_latest_image_id, save_image
from app.database import get_session
from app.images.models import Image
from app.images.schema import ImageResponse
from app.shared.detector import detect_face_locations, draw_face_boxes
from app.shared.utils import is_valid_image, save_file_to_disk


router = APIRouter(
    prefix="/images", 
    tags=["images"],
    responses={404: {'description': 'Page not found'}}
)


@router.get("/", response_model=List[ImageResponse])
def load_images(session: Session = Depends(get_session)):
    print("Loading images...")
    images = get_images(session)
    return images


@router.post("/")
def upload_image(file: UploadFile, session: Session = Depends(get_session)):
    if not file.content_type or not is_valid_image(file.file):
        return {"error": "Invalid image"}
    
    latest_id = (get_latest_image_id(session) or 0) + 1
    img_type = file.content_type.split("/")[-1]
    img_name = f"{latest_id}.{img_type}"
    image_path = os.path.join(STATIC_DIR, img_name)
    content = file.file.read()

    if not save_file_to_disk(image_path, content):
        return {"error": "Error while saving file to disk!"}
    
    positions = detect_face_locations(image_path)
    draw_face_boxes(image_path, positions)

    image = Image(
        id=latest_id, image_path=image_path, number_of_people=len(positions)
    )
    save_image(session, image)
    return {"detail": "success"}
