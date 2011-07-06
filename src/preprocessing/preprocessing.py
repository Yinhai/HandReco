# -*- coding: cp936 -*-

import Image,ImageFilter
im = Image.open("1.bmp")
print im.format, im.size, im.mode

width, height = im.size

horizontal_lines = [(0,  i, width, i + 1) for i in range(height)]

candidate_lines = []
ligible_lines = []

for line in horizontal_lines:
    region = im.crop(line)
    if region.histogram()[0] <= 10:
        region = region.point(lambda i : 0)
        im.paste(region, line)

im.show()

