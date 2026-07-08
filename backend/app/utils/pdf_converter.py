from pdf2image import convert_from_path
import os

OUTPUT_FOLDER = "outputs"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def pdf_to_image(pdf_path: str):
    pages = convert_from_path(pdf_path, dpi=300)

    image_name = os.path.basename(pdf_path).replace(".pdf", ".png")
    image_path = os.path.join(OUTPUT_FOLDER, image_name)

    pages[0].save(image_path, "PNG")

    return image_path