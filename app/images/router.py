import os
from typing import List
from fastapi import APIRouter, Depends, UploadFile
from sqlmodel import Session

from app.config import STATIC_DIR
from app.images.crud import get_images, get_latest_image_id, save_image
from app.database import get_session
from app.images.models import Image
from app.images.schema import ImageResponse
from app.utils import is_valid_image, save_file_to_disk


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
    if not is_valid_image(file.file):
        return {"error": "Invalid image"}
    
    latest_id = (get_latest_image_id(session) or 0) + 1
    image_path = os.path.join(STATIC_DIR, str(latest_id))
    content = file.file.read()
    if not save_file_to_disk(image_path, content):
        return {"error": "Error while saving file to disk!"}
    
    image = Image(id=latest_id, image_path=image_path)
    save_image(session, image)
    return {"detail": "success"}
