from numpy import sqrt, array, dot, pi, arccos, cross
from Ray_Class import Ray
from Spherical_Refraction import SphericalRefraction

'''Testing the intercept method'''

#For ray intercepting a concave lens
element = SphericalRefraction(10,0.2,1,1.5,2000)

ray = Ray([0,0,0], [0,0,1])
intercept_1 = element.intercept(ray)
#This should be [0,0,10]
#intercept_1 = [0,0,10], so the method holds for this case

ray = Ray([2,2,0], [0,0,1])
intercept_2 = element.intercept(ray)
#This should be [2,2,10.8769]
#intercept_2 = [2,2,10.8769], so the method holds for this case

#Now we can test for when the ray does not intercept the spherical lens
ray = Ray([10,0,0], [0,0,1])
intercept_3 = element.intercept(ray)
#intercept_3 is None, so the method holds for this case

#Now we can test for when the ray intercepts the theoretical spherical lens, but is larger than the aperture
element = SphericalRefraction(10,0.2,1,1.5,0.1)
ray = Ray([2,2,0], [0,0,1])
intercept_4 = element.intercept(ray)
#This is also None, so the method also holds for this case

#For ray intercepting a convex lens

#An aspect of convex lenses is that the ray can start in the sphere, in which case the code has to
#take the intercept that the ray will actually move towards, instead of a point behind the ray which
#may be closer. This case is tested in the next two intercept calculations

element = SphericalRefraction(9,-0.1,1,1.5,2000)

ray = Ray([0,0,0], [0,0,1])
intercept_5 = element.intercept(ray)
#This should be [0,0,9]
#intercept_5 = [0,0,9], so the method holds for this case

ray = Ray([2,2,0], [0,0,1])
intercept_6 = element.intercept(ray)
#This should be [2,2,8.5917]
#intercept_6 = [2,2,8.5917], so the method holds for this case

#Another aspect is that the ray can start behind the sphere, as it moves forward it will intercept it
#twice. We must of course take the second intercept as this is when the lens is convex. This case is
#tested in the next two intercept calculations

element = SphericalRefraction(10,-0.2,1,1.5,2000)

ray = Ray([0,0,0], [0,0,1])
intercept_7 = element.intercept(ray)
#This should be [0,0,10]
#intercept_7 = [0,0,10], so the method holds for this case

ray = Ray([2,2,0], [0,0,1])
intercept_8 = element.intercept(ray)
#This should be [2,2,9.1231]
#intercept_8 = [2,2,9.1231], so the method holds for this case


#Now we can test for when the ray does not intercept the spherical lens
ray = Ray([10,0,0], [0,0,1])
intercept_9 = element.intercept(ray)
#intercept_9 is None, so the method holds for this case

#Now we can test for when the ray intercepts the theoretical spherical lens, but is larger than the aperture
element = SphericalRefraction(10,-0.2,1,1.5,0.1)
ray = Ray([2,2,0], [0,0,1])
intercept_10 = element.intercept(ray)
#This is also None, so the method also holds for this case

#Now we can test for the special case where curvature = 0
element = SphericalRefraction(10,0,1,1.5,2000)

ray = Ray([0,0,0], [0,0,1])
intercept_11 = element.intercept(ray)
#This should be [0,0,10]
#intercept_11 = [0,0,10], so the method holds for this case

ray = Ray([0,0,0], [1,-1,1])
intercept_12 = element.intercept(ray)
#This should be [10,-10,10]
#intercept_12 = [10,-10,10], so the method holds for this case

#Testing for an aperture that is too small:
element = SphericalRefraction(10,0,1,1.5,2)
ray = Ray([0,0,0], [1,-1,1])
intercept_13 = element.intercept(ray)
#intercept_13 is None, so the method holds for this case

#Through this testing, we can be very confident that the intercept method works

'''Testing the refraction method'''

ray = Ray([0,-40,0], [sqrt(2)/2,sqrt(2)/2,0])
normal = array([0,-1,0])
element = SphericalRefraction(10,0.2,1,1.5,2000)

refracted_drn = element.refraction(ray, normal)
angle1 = arccos(dot(refracted_drn, -normal))/(2*pi)*360
#From manual calculation using the vector form of Snell's law, the answer should be 28.1255 degrees
#Checking if the incident, normal and refracted vectors lie on the same plane:
check = dot((cross(normal, ray.k())), refracted_drn)
#check = 0, as the triple product of the three vectors = 0 they therefore lie on the same plane
#These are all the expected results, the application of Snell's law therefore works

#For a case where total internal reflection should happen, as sin(theta) > n2/n1

element = SphericalRefraction(10,0.2,1.5,1,2000)

ray = Ray([0,0,0], [-0.8945,1,0]) #The direction does not need to be normalized as the class does it for us
angle2 = arccos(dot(ray.k(), -normal))/(2*pi)*360
refracted_drn2 = element.refraction(ray,normal)
#This should return None, as we are just above the critical angle of 41.81 degrees, at 41.8126
#This does indeed happen, confirming that this method deals well with TIR

#If we decrease this incident angle to just under 41.81 degrees, to 41.8094 degrees
ray = Ray([0,0,0], [-0.8944,1,0])
angle3 = arccos(dot(ray.k(), -normal))/(2*pi)*360
refracted_drn3 = element.refraction(ray,normal)
#There is no TIR and the method no longer returns None

#Through this testing, we can be very confident that the refraction method works

'''Manually testing the propagate_ray method'''

#This method mostly makes use of the already tested methods. The only major part is that it is here
#that the code determines the normal from the surface to the incoming ray.
#Due to the plus/minus conventions used in the refraction method, we need the normal to go against
#the incoming ray, in other words, their dot product must be 0 (a special case) or negative.

#For a curvature of 0.2, R = 5
#For an intercept of [0,0,10], the origin is at [0,0,15]
#From normal = intercept - origin, normal = [0,0,-5], which will be normalised to [0,0,-1]
#As the incoming ray will have positive z, this calculation works and will give us a normal facing
#against the ray direction

#For a curvature of -0.2, R = -5
#For an intercept of [0,0,10], the origin is at [0,0,5]
#From normal = origin - intercept, normal = [0,0,-5], which will be normalised to [0,0,-1]
#As the incoming ray will have positive z, this calculation works and will give us a normal facing
#against the ray direction

#We can therefore be very confident that the refraction method works
