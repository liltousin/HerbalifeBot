from PIL import Image


def resize_image(file_name):
    im = Image.open(file_name)
    x, y = im.size
    side = min(x, y)
    box = (x // 2 - side // 2, y // 2 - side // 2, x // 2 + side // 2, y // 2 + side // 2)
    resized_image = im.crop(box)
    resized_image.save(file_name)
