class OpticalElement:
    '''
    Groups all the individual optical elements into one optical element we can propagate rays through
    '''
    def __init__(self, elements):
        self.__elements = elements
        
    def propagate_ray(self, ray):
        '''
        propagates a ray through the optical element conssisting of smaller individual elements
        '''
        for elem in self.__elements:
            elem.propagate_ray(ray)