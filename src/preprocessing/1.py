# -*- coding: cp936 -*-

import Image

im = Image.open("A_1310206065789.png")

print im.format, im.size, im.mode
im.width, im.height = im.size

box = (0,0, im.width / 2, im.height /2)
region = im.crop(box)

region = region.transpose(Image.ROTATE_180)

im.paste(region, box)
im.show()

im = im.convert('L')

import ImageFilter
out = im.filter(ImageFilter.FIND_EDGES)
out.show()


##Filters = [ImageFilter.BLUR, ImageFilter.CONTOUR, ImageFilter.DETAIL,
##           ImageFilter.EDGE_ENHANCE, ImageFilter.EDGE_ENHANCE_MORE, ImageFilter.EMBOSS,
##           ImageFilter.FIND_EDGES, ImageFilter.SMOOTH, ImageFilter.SMOOTH_MORE, ImageFilter.SHARPEN]
##
##for Filter in Filters:
##    out = im.filter(Filter)
##    out.show()

##import ImageEnhance
##
##enhancer = ImageEnhance.Sharpness(im)
##
##for i in range(8):
##    factor = i / 4.0
##    enhancer.enhance(factor).show("Sharpness %f" % factor)

##im = im.convert('L')
##
##im.show()
##
##def f(i):
##    if i < 150:
##        return 0
##    else:
##        return 255
##im= im.point(lambda i: 0 if i < 150 else 255)
##im.show()
