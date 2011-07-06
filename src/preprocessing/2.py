# -*- coding: cp936 -*-

import Image,ImageFilter
im = Image.open("1.bmp")
print im.format, im.size, im.mode

im.width, im.height = im.size

box = (0, im.height / 2, im.width, im.height /2 + 1)

region = im.crop(box)

region = region.point(lambda i : 0)
##region = region.transpose(Image.ROTATE_180)

im.paste(region, box)
im.show()

