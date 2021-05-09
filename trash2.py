from PILasOPENCV import Image
import sys

img = Image.open(sys.argv[1])
img = img.convert("RGBA")

pixdata = img.load()

# Clean the background noise, if color != white, then set to black.

for y in xrange(img.size[1]):
    for x in xrange(img.size[0]):
        if pixdata[x, y] == (255, 255, 255, 255):
            pixdata[x, y] = (0, 0, 0, 255)