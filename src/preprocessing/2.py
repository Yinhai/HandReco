import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
from scikits.learn.svm import SVC
clf = SVC()
clf.fit(X, y)
print clf.predict([[-0.8, -1]])
