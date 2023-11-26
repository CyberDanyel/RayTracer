from Ray_Class import Ray
from numpy import array

#Check initialisation:
ray = Ray(array([0,0,0]), array([0,0,1]))
#Initialises correctly

position = ray.p() #Correctly returns current position
direction = ray.k() #Correctly returns current direction

ray.append(array([3,0,8]), array([4,0,1]))

vertices = ray.vertices() #Correctly returns an array of previous and current positions
vectors = ray.vectors() #Correctly returns an array of previous and current directions

new_position = ray.p() #Correctly returns current position
new_direction = ray.k() #Correctly returns current direction + normalises it correctly

ray.terminate_ray()
terminated_check = ray.check_if_terminated()
#Ray has been correctly terminated, and terminated_check is True, so the check method works as well