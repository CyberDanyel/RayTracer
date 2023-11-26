from Ray_Class import Ray
from numpy import array

class SimpleRayBundle:
    '''
    Creates a simple bundle of rays in the of straight lines crossing the origin x,y = 0
    '''
    def __init__(self, divider, i_range):
        self.__rays = []
        self.__divider = divider
        self.__i_range = i_range
        self.__rays.append(Ray(array([0, 0, 0]), array([0, 0, 1])))

        for i in range(self.__i_range):
            j = i + 1 #Without this, i would start at 0 and all the following lines would produce
                      #the same point
            self.__rays.append(Ray(array([j/self.__divider, 0, 0]), array([0, 0, 1])))
            self.__rays.append(Ray(array([-j/self.__divider, 0, 0]), array([0, 0, 1])))
            self.__rays.append(Ray(array([0, j/self.__divider, 0]), array([0, 0, 1])))
            self.__rays.append(Ray(array([0, -j/self.__divider, 0]), array([0, 0, 1])))
            self.__rays.append(Ray(array([j/self.__divider, j/self.__divider, 0]), array([0, 0, 1])))
            self.__rays.append(Ray(array([-j/self.__divider, -j/self.__divider, 0]), array([0, 0, 1])))
            self.__rays.append(Ray(array([j/self.__divider, -j/self.__divider, 0]), array([0, 0, 1])))
            self.__rays.append(Ray(array([-j/self.__divider, j/self.__divider, 0]), array([0, 0, 1])))
        
    def create(self):
        return self.__rays