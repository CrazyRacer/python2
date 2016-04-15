from numpy import *

randMat = mat(random.rand(4,4))

invRandMat = randMat.I
# print invRandMat
# print randMat
# print randMat*invRandMat
myEye=randMat*invRandMat
print myEye
print myEye-eye(4)
print eye(4)