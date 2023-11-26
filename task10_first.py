from numpy import array
import matplotlib.pyplot as plt
from Ray_Class import Ray
from Optical_Element import OpticalElement
from Spherical_Refraction import SphericalRefraction
from Output_Plane import OutputPlane

refractor = SphericalRefraction(100, 0.03, 1, 1.5)
output = OutputPlane(250)
optical_element = OpticalElement([refractor, output])

rays = []

rays.append(Ray(array([0, 0, 0]), array([0, 0, 1])))
rays.append(Ray(array([0.1, 0, 0]), array([0, 0, 1])))
rays.append(Ray(array([-0.1, 0, 0]), array([0, 0, 1])))

fig = plt.figure()
ax = fig.gca()


for i in range(len(rays)):
    ray = rays[i]
        
    optical_element.propagate_ray(ray)
    if ray.check_if_terminated == True:
        pass
    else:
        b = ray.vertices()

        xs = []
        zs = []
    
        for i in range(len(b)):
            xs.append(b[i][0])
            zs.append(b[i][2])

        plt.plot(xs, zs)
        
ax.set_xlabel("x (mm)")
ax.set_ylabel("z (mm)")
plt.grid()
plt.savefig('task 10')

#We can estimate the position of the paraxial focus to be at z = 200, giving us a focal length of 100
#This is exactly what we expect for the paraxial focal point of a spherical surface