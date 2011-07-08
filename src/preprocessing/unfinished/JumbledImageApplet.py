from java.io import *
from java.net import *
from java.awt import *
from java.awt.event import *
from java.awt.image import *
from javax.imageio import *
from javax.swing import *
import java.util.Random;

class JumbledImage(Component):
    def __init__(self, imageSrc):
        super(JumbledImage, self).__init__()
        self.numlocs = 2
        self.numcells = self.numlocs ** 2

        self.bi = ImageIO.read(imageSrc);
        self.w = bi.getWidth(null);
        self.h = bi.getHeight(null);

        self.cw = w/self.numlocs;
        self.ch = h/self.numlocs;
        self.cells = range(self.numcells)
    
    def jumble(self):
        rand = Random();
        for i in range(self.numcells):
            while True:
                ri = rand.nextInt(self.numlocs)
                if ri != i:
                    break

            tmp = self.cells[i]
            self.cells[i] = self.cells[ri]
            self.cells[ri] = tmp;

    def getPreferredSize(self):
        return Dimension(self.w, self.h)

    def paint(self, g):
        for x in range(self.numlocs):
            sx = x * self.cw
            for y in range(self.numlocs):
                sy = y * ch
                cell = self.cells[x*self.numlocs+y];
                dx = (cell / self.numlocs) * self.cw;
                dy = (cell % self.numlocs) * self.ch;
                g.drawImage(self.bi,
                            dx, dy, dx+self.cw, dy+self.ch,
                            sx, sy, sx+self.cw, sy+self.ch,
                            None);


class JumbledImageApplet(JApplet):

    def JumbledImageApplet(self):
        pass
    
    def JumbledImageApplet(self, imageSrc):
        self.imageSrc = imageSrc

    def __init__(self):
        self.imageFileName = "duke_skateboard.jpg";
        self.imageSrc = URL(self.getCodeBase(), self.imageFileName);
        self.buildUI();

    def buildUI(self):
        ji = JumbledImage(self.imageSrc)
        self.add("Center", ji);
        jumbleButton = JButton("Jumble");
        class ActionListener:
            def actionPerformed(self, e):
                b = JButton(e.getSource())
                ji.jumble()
                ji.repaint()
        jumbleButton.addActionListener(ActionListener())
        
        jumbleSize = ji.getPreferredSize();
        self.resize(jumbleSize.width, jumbleSize.height+40);
        self.add("South", jumbleButton);
    
    def main(s):
        f = JFrame("Jumbled Image");
        class WindowAdapter:
            def windowClosing(self, e):
                System.exit(0)
        f.addWindowListener(WindowAdapter())

        imageSrc = ((File(imageFileName)).toURI()).toURL();

        jumbler = JumbledImageApplet(imageSrc);
        jumbler.buildUI();
        f.add("Center", jumbler);
        f.pack();
        f.setVisible(true);

if __name__ == '__main__':
    applet = JumbledImageApplet()
    applet.main([])
    
