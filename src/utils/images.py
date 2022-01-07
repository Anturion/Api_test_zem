import shutil
import tempfile
from pathlib import Path

def get_images_path(image_name: str) -> str:
    
    root = Path()
    images = Path.joinpath(root, 'static/images')
    image_path = images.joinpath(image_name)
    
    return image_path.resolve()


def save_image(filename: str, file: tempfile.SpooledTemporaryFile) -> None:
    
    try:
        images_path = get_images_path(filename)
        with images_path.open("wb") as buffer:
            shutil.copyfileobj(file, buffer)
    finally:
        file.close()