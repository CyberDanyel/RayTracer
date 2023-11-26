from Output_Plane import OutputPlane
from Ray_Class import Ray
from numpy import array

test_output_plane = OutputPlane(200)

ray1 = Ray(array([0,0,0]), array([0,0,1]))
ray2 = Ray(array([-200,200,0]), array([1,-1,1]))
ray3 = Ray(array([0,0,0]), array([1,1,1]))
ray4 = Ray(array([0,0,0]), array([0,0,-1]))
ray5 = Ray(array([0,0,0]), array([1,1,0]))

rays = [ray1, ray2, ray3, ray4, ray5]

for i in range(len(rays)):
    test_output_plane.propagate_ray(rays[i])
    
#ray 1 should be propagated to [0,0,200]
#ray 2 should be propagated to [0,0,200]
#ray 3 should be propagated to [200,200,200]
#ray 4 should be terminated as it goes away from the output plane
#ray 5 should be terminated as it goes parallel to the output plane

#The results are as expected, the test is successful and the class works correctly