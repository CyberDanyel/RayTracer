from numpy import linalg

class Ray:
    
    ''' Defines an optical ray with the ability of storing current and historical
    position and direction'''
    
    def __init__(self, position, direction):
        ''' Initialises the class with a current position and direction, stores them
        in a list in order to keep track of historical positions and directions'''
        if all(v == 0 for v in direction):
            raise Exception('This ray is not moving')
        self.__position = position
        self.__direction = direction/linalg.norm(direction)
        self.__position_record = [position]
        self.__direction_record = [self.__direction]
        self.__terminated = False
    def p(self):
        '''
        Returns
        -------
        Current position (numpy array)
        '''
        return self.__position
    def k(self):
        '''
        Returns
        -------
        Current direction (numpy array)
        '''
        return self.__direction
    def append(self, new_pos, new_dir):
        '''
        Parameters
        ----------
        new_pos : numpy array
            New position of the ray
        new_dir : numpy array
            New direction of the ray
        -------
        Stores all historical positions and directions of the ray in a list by
        appending the new position
        '''
        self.__position_record.append(new_pos)
        self.__position = new_pos
        if new_dir is None:
            self.__direction = None
            self.__direction_record.append(None)
        else:
            self.__direction = new_dir/linalg.norm(new_dir)
            self.__direction_record.append(new_dir/linalg.norm(new_dir))
    def vertices(self):
        '''
        Returns
        -------
        list
            list of historical positions.
        '''
        return self.__position_record
    def vectors(self):
        '''
        Returns
        -------
        list
            list of historical directions.
        '''
        return self.__direction_record
    
    def terminate_ray(self):
        self.__terminated = True
    
    def check_if_terminated(self):
        if self.__terminated == True:
            return True
        else:
            return False
