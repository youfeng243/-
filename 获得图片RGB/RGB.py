from PIL import Image

im = Image.open('111.png')
pix = im.load()
width = im.size[0]
height = im.size[1]
for x in range(width):
    for y in range(height):
        r, g, b = pix[x, y]
        break
    break
print r << 16 | g << 8 | b

