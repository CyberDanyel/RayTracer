from Ray_Class import Ray
from numpy import array, pi, cos, sin, matmul

class ConcentricRayBundle:
    '''
    Creates a bundle of rays in the shape of concentric circles
    '''
    def __init__(self, maxrad, i_range):
        self.__rays = []
        self.__maxrad = maxrad
        self.__i_range = i_range
        self.__rays.append(Ray(array([0, 0, 0]), array([0, 0, 1])))
        for i in range(self.__i_range):
            j = i*(2*pi)/self.__i_range #So that the rotation is a full circle
            rotation_matrix = array([[cos(j), -sin(j), 0],[sin(j), cos(j), 0], [0, 0, 1]])
            for p in range(maxrad):
                self.__rays.append(Ray(matmul(array([p+1, 0, 0]), rotation_matrix), array([0, 0, 1])))
        
    def create(self):
        return self.__rays