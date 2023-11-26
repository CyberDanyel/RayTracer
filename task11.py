import matplotlib.pyplot as plt
from Optical_Element import OpticalElement
from Spherical_Refraction import SphericalRefraction
from Output_Plane import OutputPlane
from Ray_Class import Ray
from numpy import array

'''1st case:'''
refractor = SphericalRefraction(100, 0.03, 1, 1.5)
output = OutputPlane(400)
optical_element = OpticalElement([refractor, output])

ray1 = Ray(array([2,0,0]), array([-0.02,0,1]))
ray2 = Ray(array([2,0,0]), array([0,0,1]))
ray3 = Ray(array([-2,0,0]), array([0.02,0,1]))
ray4 = Ray(array([-2,0,0]), array([0,0,1]))
ray5 = Ray(array([0,2,0]), array([0,-0.02,1]))
ray6 = Ray(array([0,2,0]), array([0,0,1]))
ray7 = Ray(array([0,-2,0]), array([0,0.02,1]))
ray8 = Ray(array([0,-2,0]), array([0,0,1]))

rays = [ray1, ray2, ray3, ray4, ray5, ray6, ray7, ray8]

fig = plt.figure()
ax = fig.gca(projection='3d')


for i in range(len(rays)):
    ray = rays[i]
        
    optical_element.propagate_ray(ray)
    if ray.check_if_terminated == True:
        pass
    else:
        b = ray.vertices()

        xs = []
        ys = []
        zs = []
    
        for i in range(len(b)):
            xs.append(b[i][0])
            ys.append(b[i][1])
            zs.append(b[i][2])

        plt.plot(xs, ys, zs)
ax.set_xlabel("x (mm)")
ax.set_ylabel("y (mm)")
ax.set_zlabel("z (mm)")

plt.savefig('T-11', dpi = 800)

#We can see the image formed is inverted on the x and y axis