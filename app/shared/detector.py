import cv2
from deepface import DeepFace
from typing import List


def detect_face_locations(img_path: str) -> list:
    """
    img: image to detect faces on (numpy array)
    """
    faces = DeepFace.extract_faces(img_path=img_path, detector_backend='mtcnn')
    positions = []
    for face in faces:
        area = face['facial_area']
        x, y, w, h = area['x'], area['y'], area['w'], area['h']
        positions.append((x, y, w, h))

    return positions


def draw_face_boxes(img_path: str, positions: List) -> None:
    """
    img: image to draw box on (numpy array)
    positions: list of coordinates for each box: [x, y, w, h]
    """

    img = cv2.imread(img_path)
    for position in positions:
        x, y, w, h = position
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imwrite(img_path, img)
