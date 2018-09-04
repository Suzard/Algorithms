import prompt,re
import math
from goody import type_as_str
#Submitter edwardc6(Chen,Edward)
class Point:
    def __init__(self, x ,y ,z):
        
        if(type(x) != int):
            raise AssertionError('x is not of type {} x should be int'.format(type(x)))
        if(type(y) != int):
            raise AssertionError('y is not of type {} y should be int'.format(type(y)))
        if(type(z) != int):
            raise AssertionError('z is not of type {} z should be int'.format(type(z)))
        self.list = [(x,'x'),(y,'y'),(z,'z')]
        self.x = x
        self.y = y
        self.z = z
    def __repr__(self):
        return 'Point({},{},{})'.format(self.x,self.y, self.z)
    def __str__(self):
        return '(x={},y={},z={})'.format(self.x, self.y, self.z)

    def __bool__(self):
        d = all(i[0] != 0 for i in self.list )
        if(self.x == 0 and self.y == 0 and self.z == 0):
            return False
        else: 
            return True
        #return d
    def __add__(self, left_variable):
        if(type(left_variable) != Point):
            raise TypeError('left variable should not be type{}'.format(type(left_variable)))
        else:
            g = self.x + left_variable.x
            h = self.y + left_variable.y
            i = self.z + left_variable.z
            return Point(g,h,i)
    def __radd__(self, right_variable):

        return self + right_variable
    
    def __mul__(self, left_variable):
        if(type(left_variable) != int):
            raise TypeError('left variable should not be type{}'.format(type(left_variable)))
        else:
            g = self.x*left_variable
            h = self.y*left_variable
            i = self.z*left_variable
            return Point(g,h,i)
    def __rmul__(self,right_variable):
        return self * right_variable
    def __lt__(self, right_variable):
        if(type(right_variable) != Point and type(right_variable) != int and type(right_variable) != float):
            raise TypeError('right variable should not be type{}'.format(type(right_variable)))
        else:
            if(type(right_variable) == Point):
                t = math.sqrt( self.x*self.x + self.y*self.y + self.z*self.z)
                z = math.sqrt(right_variable.x*right_variable.x + right_variable.y*right_variable.y + right_variable.z*right_variable.z)
                return (t<z)
            else:
                t = math.sqrt( self.x*self.x + self.y*self.y + self.z*self.z)
                return (t<right_variable)
    
        
    def __getitem__(self, variable):
        if(type(variable) != int and type(variable) != str):

            raise IndexError('index should not be of type{}'.format(type(variable)))
        if(variable == 'x' or variable ==  'y' or variable == 'z'or variable == 0 or variable == 1 or variable == 2):
            if(type(variable) == str):
                if(variable in self.__dict__):
                    return self.__dict__[variable]
                else:
                    raise IndexError
            else:
                return self.list[variable][0]
            
        else:
            raise IndexError('improper value for this function')
    def __call__(self, x,y,z):
        self.__init__(x,y,z)
        return None
if __name__ == '__main__':
    # Put in simple tests for Point before allowing driver to run
    
    print()
    import driver
    
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
