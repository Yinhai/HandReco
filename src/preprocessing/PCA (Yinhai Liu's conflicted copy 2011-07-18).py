from PIL import Image
from numpy import *

def pca(X):
  # Principal Component Analysis
  # input: X, matrix with training data as flattened arrays in rows
  # return: projection matrix (with important dimensions first),
  # variance and mean

  #get dimensions
  num_data,dim = X.shape
  #center data
  mean_X = X.mean(axis=0)
  for i in range(num_data):
      X[i] -= mean_X

  if dim>100:
      print 'PCA - compact trick used'
      M = dot(X,X.T) #covariance matrix
      e,EV = linalg.eigh(M) #eigenvalues and eigenvectors
      tmp = dot(X.T,EV).T #this is the compact trick
      V = tmp[::-1] #reverse since last eigenvectors are the ones we want
      S = sqrt(e)[::-1] #reverse since eigenvalues are in increasing order
  else:
      print 'PCA - SVD used'
      U,S,V = linalg.svd(X)
      V = V[:num_data] #only makes sense to return the first num_data

  #return the projection matrix, the variance and the mean
  return V,S,mean_X

from PIL import Image
import numpy
import pylab

immatrix = numpy.array([[-5,-4], [-4,-5], [-5,-6], [-6,-5], [5,4], [4,5], [5,6], [6,5]],'f')
V,S, immean = pca(immatrix)
print "V:",V
print "S:", S
print "immean:", immean


imlist = ['A_1.png', 'A_2.png', 'A_3.png', 'A_4.png']#, 'B_1.png', 'B_2.png', 'B_3.png', 'B_4.png']
im = numpy.array(Image.open(imlist[0])) #open one image to get the size
m,n = im.shape[0:2] #get the size of the images
imnbr = len(imlist) #get the number of images

#create matrix to store all flattened images
immatrix = numpy.array([numpy.array(Image.open(imlist[i])).flatten() for i in range(imnbr)],'f')

#perform PCA
V,S,immean = pca(immatrix)

print V.shape
#mean image and first mode of variation
immean = immean.reshape(m,n)
mode = V[0].reshape(m,n)


# im = Image.new("L", (100, 100))
# im.putdata(list(V[0]))
# print im.size
# im.show()

#Image0 = numpy.array(Image.open(imlist[0]))
# #show the images
# pylab.figure()
# pylab.gray()
# pylab.imshow(Image0)
# ##pylab.imshow(immean)
# ##
# ##pylab.figure()
# ##pylab.gray()
# ##pylab.imshow(mode)
# ##
# pylab.show()
