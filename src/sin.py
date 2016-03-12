
import math
import matplotlib.pyplot as plt
x = [float(i) / 100.0 for i in range(-300, 300)]
y = [math.sin(i) for i in x]
z = [math.tan(i) for i in x]
h = [i for i in x]
plt.plot(x,y,'g-')
plt.plot(x,z)
plt.plot(x,h)
plt.show()
