import matplotlib.pyplot as plt
from Optical_Element import OpticalElement
from Spherical_Refraction import SphericalRefraction
from Output_Plane import OutputPlane
from Concentric_Ray_Bundle import ConcentricRayBundle

refractor = SphericalRefraction(100, 0.03, 1, 1.5)
output = OutputPlane(200)
optical_element = OpticalElement([refractor, output])

rays = ConcentricRayBundle(5, 30).create()

fig = plt.figure()
ax = fig.gca()

xs = []
ys = []


for i in range(len(rays)):
    ray = rays[i]
        
    optical_element.propagate_ray(ray)
    if ray.check_if_terminated == True:
        pass
    else:
        b = ray.vertices()
        xs.append(b[2][0])
        ys.append(b[2][1])

        plt.plot(xs, ys, '.', color = 'red')
        
ax.set_xlabel("x (mm)")
ax.set_ylabel("y (mm)")
ax.axis('equal')
plt.grid()
plt.savefig('T-13', dpi = 800)

rays = ConcentricRayBundle(5, 30).create()

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

plt.savefig('T-12', dpi = 800)