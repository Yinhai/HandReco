# -*- coding: cp936 -*-

import Image,ImageFilter

Image_filename = "A_1.png"
im = Image.open(Image_filename)
print im.format, im.size, im.mode

width, height = im.size

##im.show()
def getInfo(Image_filename):
    im = Image.open(Image_filename)
    width, height = im.size
    im_1, im_2, im_3, im_4 = im.crop(0,0, height / 2, width / 2), im.crop(0, width / 2, height / 2,  
    print im.histogram()[0], im.histogram()[255]

getInfo("A_1.png")
getInfo("A_2.png")
getInfo("A_3.png")
getInfo("A_4.png")

getInfo("B_1.png")
getInfo("B_2.png")
getInfo("B_3.png")
getInfo("B_4.png")
##for line in horizontal_lines:
##    region = im.crop(line)
##    if region.histogram()[0] <= 10:
##        candidate_lines.append(line)
##        

##for line in candidate_lines[1:]:
##    if line[1] - previous_line[1] > MAX_WIDTH / 2:
##        ligible_lines.append(line)
##        previous_line = line
##
##for line in ligible_lines:
##    region = region.point(lambda i : 0)
##    im.paste(region, line)
##
##im.show()

