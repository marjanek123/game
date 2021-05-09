import cv2
import os
import numpy as np
import PILasOPENCV
import os
#from PIL import Image
SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'scrm2.jpg'

logoIm = PILasOPENCV.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size

for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) \
          or filename == LOGO_FILENAME:
        continue # skip non-image files and the logo file itself

    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        im = PILasOPENCV.open(filename)
        width, height = im.size
        print('Adding logo to %s...' % (filename))
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

                # Save changes.
        im.save(os.path.join('withLogo', filename))
        im.show()