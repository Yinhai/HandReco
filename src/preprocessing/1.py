import pylab as pl

from scikits.learn import datasets
from scikits.learn.decomposition import PCA
from scikits.learn.lda import LDA

from PIL import Image
import numpy

import os
import os.path

rootdir = "character_examples/"

AtoZ = ["A","B"]
rootdirAtoZ = [rootdir + character for character in AtoZ]

imagefilenames = []

for folder in rootdirAtoZ:
    filenames = os.listdir(folder)
    filenames = [folder + '/' + filename for filename in filenames if filename.endswith(".png")]
    imagefilenames += filenames

im = numpy.array(Image.open(imagefilenames[0])) #open one image to get the size
m,n = im.shape[0:2] #get the size of the images
imnbr = len(imagefilenames) #get the number of images

#create matrix to store all flattened images
immatrix = numpy.array([numpy.array(Image.open(imagefilenames[i])).flatten() for i in range(imnbr)],'f')

X = immatrix

pca= PCA(n_components = 10)
X_r = pca.fit(X).transform(X)

print X_r.shape

print 'explained variance ratio (first two components):', \
    pca.explained_variance_ratio_

pl.figure()

X_1 = X_r.T[0]
X_2 = X_r.T[1]

colors = 'r' * 104 + 'b'* 104

z = numpy.array([color for color in colors])

pl.scatter(X_1, X_2, s=80, c=z, marker=">")
pl.legend()
pl.title('PCA of characters')
pl.show()

