from Optical_Element import OpticalElement
import numpy as np

class OutputPlane(OpticalElement):
    '''
    Calculates the intercept of rays with the output plane and propagates them to it
    '''
    def __init__(self, plane_z):
        self.__plane_point = [0, 0, plane_z]
        self.__plane_normal = [0, 0, 1]
        
    def intercept(self, ray):
        k = ray.k()
        test_dot = (np.dot(k, self.__plane_normal))
        if test_dot <= 0:
            ray.terminate_ray()
        else:
            
            __d = (np.dot((self.__plane_point - ray.p()), self.__plane_normal))/test_dot
            intercept = ray.p() + __d*k
            return intercept
    
    def propagate_ray(self, ray):
        intercept = self.intercept(ray)
        ray.append(intercept, None)