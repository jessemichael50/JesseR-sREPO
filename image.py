from PIL import Image
from PIL import ImageFilter
# Removed invalid import statement


with Image.open("Batman 1.jpeg") as img:
    img = img.rotate(270)
    img = img.filter(ImageFilter.BLUR)
    img.save("out.jpeg")



