class Sparse_Matrix:
    def __init__(self,rows,cols,*rcv_triples):
        if(type(rows) != int or type(cols) != int):
            raise AssertionError
        if(rows <= 0 or cols <= 0):
            raise AssertionError
    
        self.rows = rows
        self.cols = cols
        z = dict()
        j = []
        for i,c,v in rcv_triples:
            if(v == 0):
                pass
            else:
                if((i,c) in j):
                    raise AssertionError
                if(i>= self.rows or c >=self.cols):
                    raise AssertionError
                z[(i,c)] = v 
                j.append((i,c))
        self.matrix = z
            
            
    
    
    def size(self):
        return (self.rows, self.cols)
    
    def __len__(self):
        return self.rows*self.cols
    
    # I have written str(...) because it is used in the bsc.txt file and
    #   it is a bit subtle to get correct. This function does not depend
    #   on any other method in this class being written correctly, although
    #   it could be simplified by using __getitem__.   
    def __str__(self):
        size = str(self.rows)+'x'+str(self.cols)
        width = max(len(str(self.matrix.get((r,c),0))) for c in range(self.cols) for r in range(self.rows))
        return size+':['+('\n'+(2+len(size))*' ').join ('  '.join('{num: >{width}}'.format(num=self.matrix.get((r,c),0),width=width) for c in range(self.cols))\
                                                                                             for r in range(self.rows))+']'

    # You may use this method for debugging purpose: its string shows the size of
    # of the Sparse_Matrix, its .matrix dictionary, and all its values as a tuple of
    # tuples.
    def details(self):
        return str(self.rows)+'x'+str(self.cols)+' -> '+str(self.matrix)+' -> '+\
               str(tuple(tuple(self.matrix.get((r,c),0) for c in range(self.cols)) for r in range(self.rows)))

    def __repr__(self):
        z = 'Sparse_Matrix('
        z += str( self.rows)
        z+= ','
        z += str(self.cols)
        z += ','
        
        for i in self.matrix:
            t = (i[0],i[1], self.matrix[(i[0],i[1])])
            z +=  str(t)
            z += ','
        z = z[0:-1]
        z += ')'
        return z

    def __iter__(self):
        for i in sorted(self.matrix, key = lambda x: self.matrix.get(x)):
            yield (i[0],i[1], self.matrix[(i[0],i[1])])
            
    def __getitem__(self,index):
        if(len(index) != 2):
            raise TypeError
        for i in index:
            if(type(i) != int):
            
                raise TypeError
            if(i<0):
                raise TypeError
        if(index[0] >= self.rows or index[1] >= self.cols):
            print(index[0],index[1])
            raise TypeError
        if(index in self.matrix):
            return self.matrix[index]
        else:
            return 0
    
    def __setitem__(self,index,value):
        if(len(index) != 2):
            raise TypeError
        for i in index:
            if(type(i) != int):
            
                raise TypeError
            if(i<0):
                raise TypeError
        if(index[0] >= self.rows or index[1] >= self.cols):
            raise TypeError
        if(index in self.matrix):
            if(value == 0):
                del [self.matrix[index]]
            else:
                self.matrix.update({index:value})
        if(index not in self.matrix):
            if(value != 0):
                self.matrix.update({index:value})
            

        
    def __add__(self,right):
        if(type(right) != int and type(right) != float and type(right) != Sparse_Matrix):
            raise TypeError
        if(type(right) == Sparse_Matrix):
            if(right.cols != self.cols or right.rows != self.rows):
                raise AssertionError
            t = Sparse_Matrix(right.rows, right.cols)
            g = dict()
            for i in range(self.rows):
                for k in range(self.cols):
                    t[i,k] = self[i,k] + right[i,k]
                    
            return t
        elif(type(right) == int or type(right) == float):
            t = Sparse_Matrix(self.rows, self.cols)

            for i in range(self.rows):
                for k in range(self.cols):
                    t[i,k] = self[i,k] + right 
            return t
            


    def __radd__(self,left):
        return self + left
    
    def __eq__(self,right):
        if(type(right) != int and type(right) != float and type(right) != Sparse_Matrix):
            raise TypeError
        if(type(right) == Sparse_Matrix):
            return self.matrix == right.matrix 
        else:
            if(right == 0):
                if(len(self.matrix) == 0):
                    return True
                return False
            else:
                for i in self.matrix:
                    if(self.matrix[i] != right):
                        return False
                if(right != 0 and len(self.matrix) != self.rows*self.cols):
                    
                    return False
                return True
    

if __name__ == '__main__':
    #Simple tests before running driver
#     m = Sparse_Matrix(3,3, (0,0,1),(1,1,3),(2,2,1))
#     print(m)
#     print(repr(m))
#     print(m.details())
#   
#     print(m.size(),len(m))
#     
#     for r,c,v in m:
#         print(r,c,v)
#     print(m[1,1])
#     m[1,1] = 0
#     m[0,1] = 2
#     print(m.details())
#     
#     print(m)
#     print(m+m)
#     print(m+1)
#     print(m==m)
#     print(m==1)
#     print()
    
    #driver tests
    import driver
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()        # import random
