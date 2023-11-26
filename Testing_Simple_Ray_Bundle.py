from Simple_Ray_Bundle import SimpleRayBundle
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

''' In order to test this class, we will just produce a plot of the xy coordinates of each ray at their
    initial positions. This should produce 8 lines crossing at the centre '''

rays = SimpleRayBundle(10, 10).create()
#This should produce 4 lines
#The vertical and horizontal lines should have a separation between each point on each individual
#line of 0.1 mm
#The diagonal lines should have a separation between each point on each individual line of sqrt(2), in
#other words, delta(x) = 0.1 and delta(y) = 0.1 as well
#Each line should pass through the centre, and range from - 1 to 1 mm 
#There should be a point at (0,0)

xs,ys = [], []

fig, ax = plt.subplots()
for i in range(len(rays)):
    ray = rays[i]
    b = ray.vertices()
    xs.append(b[0][0])
    ys.append(b[0][1])
    ax.plot(xs, ys, '.', color = 'red')

ax.tick_params(direction='in', top=True, right=True, which='both')
ax.xaxis.set_major_locator(MultipleLocator(0.1))
ax.yaxis.set_major_locator(MultipleLocator(0.1))
plt.grid()

#The result is as expected, the test is successful and the class works correctly
