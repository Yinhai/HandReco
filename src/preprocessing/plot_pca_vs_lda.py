print __doc__

import pylab as pl

from scikits.learn import datasets
from scikits.learn.decomposition import PCA
from scikits.learn.lda import LDA

iris = datasets.load_iris()

X = iris.data
print X.shape
y = iris.target

target_names = iris.target_names
print target_names
pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)

lda = LDA(n_components=2)
X_r2 = lda.fit(X, y).transform(X)

# Percentage of variance explained for each components
print 'explained variance ratio (first two components):', \
    pca.explained_variance_ratio_

print X_r.shape, y.shape
pl.figure()
for c, i, target_name in zip("rgb", [0, 1, 2], target_names):
    pl.scatter(X_r[y == i, 0], X_r[y == i, 1], c=c, label=target_name)
pl.legend()
pl.title('PCA of IRIS dataset')

pl.figure()
for c, i, target_name in zip("rgb", [0, 1, 2], target_names):
    pl.scatter(X_r2[y == i, 0], X_r2[y == i, 1], c=c, label=target_name)
pl.legend()
pl.title('LDA of IRIS dataset')

pl.show()
