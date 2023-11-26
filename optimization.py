from numpy import sqrt, linspace
import scipy.optimize as op
from Optical_Element import OpticalElement
from Spherical_Refraction import SphericalRefraction
from Output_Plane import OutputPlane
import matplotlib.pyplot as plt
from scipy import interpolate
from Concentric_Ray_Bundle import ConcentricRayBundle

xs = []
ys = []
RMS_radii = []

guess = [0.01, 0.01]

def rms_finder(curvatures):
    
    rays = ConcentricRayBundle(5, 30).create()

    plano_convex_lens1 = SphericalRefraction(100, curvatures[0], 1, 1.5168)
    plano_convex_lens2 = SphericalRefraction(105, -curvatures[1], 1.5168, 1)

    output = OutputPlane((h+3)*multiplier) #So the first focal length is 50 when multiplier = 50
    optical_element = OpticalElement([plano_convex_lens1, plano_convex_lens2, output])
    
    square_radius_sum = 0
    for i in range(len(rays)):
        ray = rays[i]
        
        optical_element.propagate_ray(ray)

        if ray.check_if_terminated == True:
            pass
        else:
            b = ray.vertices()
            square_radius_sum = square_radius_sum + ((b[3][0])**2+(b[3][1])**2)
            
    RMS_radius = sqrt(square_radius_sum/len(rays))
    return RMS_radius

focal_lengths = []
curvature1s = []
curvature2s = []
#Can only carry out a limited optimization range as it takes very long to run
optimization_range = 9
multiplier = 50
for h in range(optimization_range):
    a = op.minimize(rms_finder, guess, method = 'TNC', bounds = [(0, 0.024), (0, 0.024)])
    #The bounds are set to a max absolute curvature of 0.024, as anything greater than that
    #would cause the surfaces to cross each other, and an error in which the first surface is
    #actually farther than the second surface occurs, so a propagating ray intercepts the second surface
    #before the first one
    RMS_radii.append(a.fun)
    focal_lengths.append(((h+3)*multiplier)-100)
    curvature1s.append(a.x[0])
    curvature2s.append(a.x[1])

fig, ax = plt.subplots()
xnew = linspace((3)*multiplier-100, (optimization_range+2)*multiplier-100, num = 1000, endpoint = True)
f2 = interpolate.interp1d(focal_lengths, RMS_radii, kind = 'linear')
plt.plot(xnew, f2(xnew), label = 'Linear Interpolation', color = 'blue')
plt.plot(focal_lengths, RMS_radii, 'x', label = 'Data', color = 'red', markersize = 10)
ax.set_xlabel('Focal Length (mm)')
ax.set_ylabel('RMS of Radii (mm)')
plt.grid()
plt.legend()
plt.savefig('RMS Radii Against Focal Lengths ')