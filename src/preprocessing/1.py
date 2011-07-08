
from java.awt import *
from java.awt.event import *
from java.awt.image import *
from java.io import *
from javax.imageio import *
from javax.swing import *

img = ImageIO.read(open("1.bmp"));
 
print img.getWidth(), img.getHeight()

cellWidth = img.getWidth()  / 2
cellHeight = img.getHeight() /2

