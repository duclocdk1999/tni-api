from sqlmodel import Session, select, func
from app.images.models import Image


def save_image(session: Session, image: Image):
    session.add(image)
    session.commit()
    session.refresh(image)
    return image

def get_latest_image_id(session: Session):
    return session.exec(select(func.max(Image.id))).first()


def get_images(session: Session):
    return session.exec(select(Image)).all()


def get_image(session: Session, image_id: int):
    return session.exec(select(Image).where(Image.id == image_id)).first()


def delete_image(session: Session, image_id: int):
    image = get_image(session, image_id)
    if image:
        session.delete(image)
        session.commit()
        return True
    return False