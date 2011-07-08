'''/*
 * Part of the Java Image Processing Cookbook, please see
 * http://www.lac.inpe.br/~rafael.santos/JIPCookbook.jsp
 * for information on usage and distribution.
 * Rafael Santos (rafael.santos@lac.inpe.br)
 */'''

from java.awt.image.BufferedImage import *;
import java.awt.image.WritableRaster;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

'''
/**
 * This application creates a pure black-and-white image. In this image all pixels values are 
 * either zero (black) or one (white).
 * The JAI API is not used in this example.
 */'''

#class CreateBWImageNoJAI:
#def  main(self, args):

width = 400;
height = 400;
im =  BufferedImage(width,height,BufferedImage.TYPE_BYTE_BINARY);
raster = im.getRaster();
for h in range(height):
    for w in range(width):
        if (h / 50 + w / 50) % 2 == 0:
            raster.setSample(w,h,0,0);
        else:
            raster.setSample(w,h,0,1);
try:
    ImageIO.write(im,"PNG", File("checkboard.png"));
except IOException:
    print "can not open the file"


#if __name__ == '__main__':
    # c = CreateBWImageNoJAI()
    # c.main(None)

