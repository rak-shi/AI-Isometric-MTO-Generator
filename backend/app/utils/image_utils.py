from PIL import Image, ImageEnhance


def enhance_image(image_path: str):
    image = Image.open(image_path)

    image = image.convert("RGB")

    contrast = ImageEnhance.Contrast(image)
    image = contrast.enhance(1.5)

    sharpness = ImageEnhance.Sharpness(image)
    image = sharpness.enhance(2.0)

    image.save(image_path)

    return image_path