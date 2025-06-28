from main import *
from PIL import Image, ImageDraw

with open("test.nbm", "rb") as file:
    content = file.read()
    print(content)
    meta = read(content)
    print(meta)

width = meta[0]["iw"]
palette = meta[1]
pixels = len(meta[2])
height = pixels // width if pixels % width == 0 else (pixels // width) + 1

image = None

image = Image.new("RGBA", (width, height), (0, 0, 0, 0)) if meta[0]["ia"] else Image.new("RGB", (width, height), (0, 0, 0, 0))

for y in range(0, height):
    for x in range(0, width):
        draw = ImageDraw.Draw(image)
        pixel = meta[2][(y * height) + x]
        draw.point((x, y), palette[pixel])

image.show()