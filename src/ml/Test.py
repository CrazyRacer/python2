import kNN
import numpy
import matplotlib
import matplotlib.pyplot as plt

print kNN.classify0([0, 0], numpy.array([[1, 0], [2, 1]]), ['A', 'B'], 1)

datingDataMat, datingLabels = kNN.file2matrix('test2.txt')
# datingDataMat = numpy.zeros((3,3))
# datingDataMat[2,:] = [2,1,0]
# print datingDataMat ,datingDataMat[:,2]
print datingLabels
print 15.0*numpy.array(datingLabels)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2],15.0*numpy.array(datingLabels),15.0*numpy.array(datingLabels))
plt.show()

# ax.scatter([2,3,1],[3,1,2])
