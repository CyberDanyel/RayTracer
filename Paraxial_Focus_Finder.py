from Ray_Class import Ray
from numpy import array
from Output_Plane import OutputPlane
from Optical_Element import OpticalElement

class ParaxialFocusFinder:
    '''
    Is used to find the paraxial focus of an optical element through the find() method
    '''
    def __init__(self, elements):
        self.__elements = elements
        if len(self.__elements) == 1: #For just one refracting element
            self.__element1 = elements[0]
            self.__output = OutputPlane(250)
            self.__optical_element = OpticalElement([self.__element1, self.__output])
        elif len(self.__elements) == 2: #For two refracting elements
            self.__element1 = elements[0]
            self.__element2 = elements[1]
            self.__output = OutputPlane(250)
            self.__optical_element = OpticalElement([self.__element1, self.__element2, self.__output])
        else:
            raise Exception('Number of elements not applicable')
    def find(self):
        #Finding the paraxial focus
        self.__ray = (Ray(array([0.1, 0, 0]), array([0, 0, 1])))
        self.__optical_element.propagate_ray(self.__ray)
        b = self.__ray.vertices()
        if len(self.__elements) == 2:        
            self.__m = (b[3][2]-b[2][2])/(b[3][0]-b[2][0])
            self.__c = b[2][2]-self.__m*b[2][0]
            return self.__c
        else:
            self.__m = (b[2][2]-b[1][2])/(b[2][0]-b[1][0])
            self.__c = b[1][2]-self.__m*b[1][0]
            return self.__c
        