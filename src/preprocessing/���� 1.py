print __doc__

import pylab as pl

from scikits.learn import datasets
from scikits.learn.decomposition import PCA
from scikits.learn.lda import LDA

from PIL import Image
import numpy

imlist = ['A_1.png', 'A_2.png', 'A_3.png', 'A_4.png', 'B_1.png', 'B_2.png', 'B_3.png', 'B_4.png']
im = numpy.array(Image.open(imlist[0])) #open one image to get the size
m,n = im.shape[0:2] #get the size of the images
imnbr = len(imlist) #get the number of images

#create matrix to store all flattened images
immatrix = numpy.array([numpy.array(Image.open(imlist[i])).flatten() for i in range(imnbr)],'f')

X = immatrix

pca= PCA(n_components = 10)
X_r = pca.fit(X).transform(X)
print X_r
print 'explained variance ratio (first two components):', \
    pca.explained_variance_ratio_

pl.figure()

X_1 = X_r.T[0]
X_2 = X_r.T[1]

target_names = ['A', 'B']
z = numpy.array(['r', 'r', 'r','r', 'b','b','b','b'])

pl.scatter(X_1, X_2, s=80, c=z, marker=">")
# for c, i, target_name in zip("rb", [0,1], target_names):
#     #pl.scatter(X_1,X_2,s=80, c='r', marker=">")
#     pl.scatter(X_r[y == i, 0], X_r[y == i, 1], c=c, label=target_name)
pl.legend()
pl.title('PCA of IRIS dataset')

# lda = LDA(n_components=2)
# y = numpy.array(['A', 'A', 'A','A', 'B','B','B','B'])
# y = numpy.array([0,0,0,0,1,1,1,1])
# X_r2 = lda.fit(X, y).transform(X)

# X_1 = X_r2.T[0]
# X_2 = X_r2.T[1]

# pl.figure()
# pl.scatter(X_1, X_2, s=80, c=z, marker=">")
# # for c, i, target_name in zip("rgb", [0, 1, 2], target_names):
# #     pl.scatter(X_r2[y == i, 0], X_r2[y == i, 1], c=c, label=target_name)
# pl.legend()
# pl.title('LDA of IRIS dataset')

pl.show()
