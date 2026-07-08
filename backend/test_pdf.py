from app.utils.pdf_converter import pdf_to_image

pdf_path = "uploads/3. Marked isometric (1).pdf"

image_path = pdf_to_image(pdf_path)

print("Image created at:", image_path)