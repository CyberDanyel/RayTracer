from Optical_Element import OpticalElement
import numpy as np
import math

def check_if_negative(number):
    if number < 0:
        return True
    else:
        return False

class SphericalRefraction(OpticalElement):
    '''
    Is used to instantiate optical elements, has methods to find the intercept of a ray with the 
    element and to find the refracted ray from the element
    '''
    
    def __init__(self, z0, curvature, n1, n2, aperture_radius = np.inf):
        self.__z0 = z0
        self.__curvature = curvature
        self.__n1 = n1
        self.__n2 = n2
        self.__aperture_radius = aperture_radius
        #We must establish a point on the plane first, we know the point at
        #which the plane intercepts the z axis, so:
        self.__plane_point = np.array([0, 0, self.__z0])
        #we must also establish a normal to the plane, which is:
        self.__plane_normal = np.array([0, 0, 1])
        if curvature != 0:
            self.__R = 1/self.__curvature
        
    def intercept(self, ray):
        k = ray.k()
        #If the curvature is 0, as R = 1/curvature, the program will try to divide
        #1/0, which will therefore result in an error. We will solve this by
        #treating it as a special case with an if statement
        #print(ray.direction)
        #if k is None:
         #   return
        if self.__curvature == 0:
            #Ray intersects a plane, we can just use established formulae to
            #find the point of intersection
            #testing if the line intercepts the plane or not:
            if np.dot(k, self.__plane_normal) == 0:
                #no intercept
                return None
            elif np.dot(k, self.__plane_normal) < 0:
                #no intercept
                return None
            else:
                d = (np.dot((self.__plane_point - ray.p()), self.__plane_normal))/(np.dot(k, self.__plane_normal))
                intercept = ray.p() + d*k
                if intercept[0] > self.__aperture_radius:
                    print('x too large')
                    return None
                elif intercept[1] > self.__aperture_radius:
                    print('y too large')
                    return None
                else:
                    return intercept
        else:
            Origin = np.array([0, 0, self.__z0 + self.__R])
            '''
            if check_if_negative(self.R) == False:
                r = ray.position - Origin #NOT SURE
            else:
                r = Origin - ray.position #NOT SURE
            '''
            r = ray.p() - Origin
            #in the equation given in task 4, if there is no intercept, the 
            #square root in the equation will have an argument less than 1
            #and will therefore result in an imaginary number
            test_square_root = np.sqrt(((np.dot(r, k))**2)-(((np.linalg.norm(r))**2)-(self.__R**2)))
            if math.isnan(test_square_root) == True:
                return None
            else:
                l_plus = -np.dot(r, k) + test_square_root
                l_minus = -np.dot(r, k) - test_square_root
                #Any negative l will go backwards in the ray and therefore is
                #not meaningful, we will therefore exclude these
                l_plus_check = check_if_negative(l_plus)
                l_minus_check = check_if_negative(l_minus)
                if l_plus_check == True:
                    if l_minus_check == True:
                        print('both l negative')
                        return None
                    else:
                        l_used = l_minus
                elif l_minus_check == True:
                    if l_plus_check == True:
                        print('both l negative')
                        return None
                    else:
                        l_used = l_plus
                else:
                    if check_if_negative(self.__R) == False:
                    #smallest positive l gives the first intercept
                        l_used = min(l_plus, l_minus)
                    else:
                        l_used = max(l_plus, l_minus)
                
                intercept = ray.p() + l_used*k
                    #This intercept is for a sphere, but we have to remember that the
                #lens ends at the aperture radius, therefore
                
                if l_plus == l_minus:
                    print('ray is tangent to the element')
                    return None
                elif intercept[0] > self.__aperture_radius:
                    print('x too large')
                    return None
                elif intercept[1] > self.__aperture_radius:
                    print('y too large')
                    return None
                    
                else:
                    return intercept

    def refraction(self, ray, normal):
        k = ray.k()
        #Calculating the angle between the ray and plane normal
        c = -np.dot(normal, k)
        r = self.__n1/self.__n2
        determinant = np.sqrt(1-((r**2)*(1-(c**2))))
        if math.isnan(determinant) == True:
            return None
        else:
            refracted_ray = r*k + (r*c - determinant)*normal
            refracted_ray = refracted_ray/np.linalg.norm(refracted_ray)
            return refracted_ray
        
    def propagate_ray(self, ray):
        #print(self.curvature)
        if self.__curvature == 0:
            intercept = self.intercept(ray)
            refracted_direction = self.refraction(ray, np.array([0, 0, -1]))
            ray.append(intercept, refracted_direction)
            
        else:
            
            origin = np.array([0, 0, self.__z0 + self.__R])
            intercept = self.intercept(ray)
            #Terminate the ray if it has no valid intercept
            if intercept is None:
                ray.terminate_ray()
                return
            else:
                if check_if_negative(self.__R) == False:
                    normal = intercept - origin
                else:
                    normal = origin - intercept
                
            normal = normal/np.linalg.norm(normal)
            refracted_direction = self.refraction(ray, normal)
            #Terminate the ray if it has no valid refraction
            if refracted_direction is None:
                ray.terminate_ray()
            else:
                ray.append(intercept, refracted_direction)
