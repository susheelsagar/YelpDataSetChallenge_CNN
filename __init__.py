__author__ = 's'
import numpy as np

x = np.array([[[1, 2, 3], [4, 5, 6]],[[1, 2, 3], [4, 5, 6]]], np.int32)
print x.shape,type(x)

f= open('stars_review.txt','r+')
stars = []
for line in f:
    stars.append(line[0])
x=np.asarray(stars)
print x.shape,x