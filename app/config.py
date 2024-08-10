import pathlib

BASE_DIR = pathlib.Path(__file__).resolve(strict=True).parent.parent

IMAGE_DIR = BASE_DIR / "images"

ICON_FILE = IMAGE_DIR / "icon.png"
TRASH_FILE = IMAGE_DIR / "trash.png"
