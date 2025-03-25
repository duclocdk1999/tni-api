import filetype
import os

def is_valid_image(content: bytes) -> bool:
    try:
        if not filetype.is_image(content):
            return False
        return True

    except Exception as e:
        return False
    

def get_file_name(file_path: str) -> str:
    return file_path.split("/")[-1]


def remove_file_from_disk(file_path: str) -> bool:
    try:
        os.remove(file_path)
        return True

    except Exception as e:
        print(f"Error while removing file from disk: {e}")
        return False


def save_file_to_disk(file_path: str, content: bytes) -> bool:
    try:
        with open(file_path, "wb") as f:
            f.write(content)
        return True

    except Exception as e:
        print(f"Error while save file to disk: {e}")
        remove_file_from_disk(file_path=file_path)
        return False