from Optical_Element import OpticalElement
from Spherical_Refraction import SphericalRefraction
from Output_Plane import OutputPlane
from Ray_Class import Ray
from numpy import array

#For a ray that shouldn't be refracted
refractor = SphericalRefraction(100, 0.03, 1, 1.5)
output = OutputPlane(250)
optical_element = OpticalElement([refractor, output])

ray1 = Ray(array([0,0,0]), array([0,0,1]))
optical_element.propagate_ray(ray1)
vertices1 = ray1.vertices()
vectors1 = ray1.vectors()
#The propagation works

#For a ray that should be refracted and is parallel to the optical axis
ray2 = Ray(array([1,2,0]), array([0,0,1]))
optical_element.propagate_ray(ray2)
vertices2 = ray2.vertices()
vectors2 = ray2.vectors()
#The propagation works

#For a ray that should be refracted and is not parallel to the optical axis
ray3 = Ray(array([1,2,0]), array([0.2,0.1,1]))
optical_element.propagate_ray(ray3)
vertices3 = ray3.vertices()
vectors3 = ray3.vectors()
#The propagation works

#Through this testing, we can be very confident that the OpticalElement class works as intended
