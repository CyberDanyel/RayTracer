from numpy import array, sqrt
import matplotlib.pyplot as plt
from Ray_Class import Ray
from Optical_Element import OpticalElement
from Spherical_Refraction import SphericalRefraction
from Output_Plane import OutputPlane
from Concentric_Ray_Bundle import ConcentricRayBundle
from Paraxial_Focus_Finder import ParaxialFocusFinder

plano_convex_lens = SphericalRefraction(100, 0.02, 1, 1.5168)

plane = SphericalRefraction(105, 0, 1.5168, 1)

output = OutputPlane(250)

optical_element = OpticalElement([plano_convex_lens, plane, output])

output = OutputPlane(ParaxialFocusFinder([plano_convex_lens, plane]).find())

optical_element = OpticalElement([plano_convex_lens, plane, output])

rays = ConcentricRayBundle(5, 30).create()

fig = plt.figure()
ax = fig.gca(projection='3d')


for i in range(len(rays)):
    ray = rays[len(rays) - (i+1)]
        
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

plt.savefig('T-15 Convex Then Plane', dpi = 800)

'''
Estimate paraxial focus
'''
rays = []

rays.append(Ray(array([0, 0, 0]), array([0, 0, 1])))
rays.append(Ray(array([0.1, 0, 0]), array([0, 0, 1])))
rays.append(Ray(array([-0.1, 0, 0]), array([0, 0, 1])))

fig, ax = plt.subplots()


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

        plt.plot(xs, zs)
        
ax.set_xlabel("x (mm)")
ax.set_ylabel("z (mm)")

#plt.savefig('task15showfocallength')

fig, ax = plt.subplots()

rays = ConcentricRayBundle(5, 30).create()

xs = []
ys = []

square_radius_sum = 0

for i in range(len(rays)):
    ray = rays[i]
        
    optical_element.propagate_ray(ray)
    
    if ray.check_if_terminated == True:
        pass
    else:
        b = ray.vertices()
        xs.append(b[3][0])
        ys.append(b[3][1])
        square_radius_sum = square_radius_sum + ((b[3][0])**2+(b[3][1])**2)
        plt.plot(xs, ys, '.', color = 'red')
        
ax.set_xlabel("x (mm)")
ax.set_ylabel("y (mm)")
ax.axis('equal')
plt.grid()
plt.savefig('T-15 Spot Diagram Convex Then Plane', dpi = 800)
RMS_radius = sqrt(square_radius_sum/len(rays))        