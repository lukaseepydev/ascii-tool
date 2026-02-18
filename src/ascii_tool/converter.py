import logging
from PIL import Image

ascii_symbols = [" ","-","•","+","=","#","@"]

logger = logging.getLogger(__name__)

def convert(img_path : str, width : int = 120):
    logger.info(f"Opening image '{img_path}...'")

    img = Image.open(img_path)
    width, height = img.size
    logger.info("Converting image to grayscale...")
    img = img.convert("L")

    new_width = 120
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)

    logger.info(f"Resizing image to {new_width} x {new_height}...")

    img = img.resize((new_width, new_height))

    logger.info("Calculating brightness for each pixel and assigning symbol...")

    pixels = img.load()

    ascii_art = ""

    for y in range(new_height):
        for x in range(new_width):
            brightness = pixels[x, y]  # value 0–255
            level = brightness * len(ascii_symbols) // 256
            logger.debug(f"({x},{y}) has a brightness of {brightness}, getting assigned {ascii_symbols[level]}.")
            ascii_art += ascii_symbols[level]

        ascii_art += "\n"

    logger.info("Conversion successful")

    return ascii_art