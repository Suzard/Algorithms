from collections import defaultdict
from goody import type_as_str

class Bag:
    def __init__(self, iter = []):
        self.bag = defaultdict(int)
        for i in iter:
            self.bag[i] += 1 
    def __repr__(self):
        z = []
        for i in self.bag:
            for t in range(self.bag[i]):
                z.append(i)
        return 'Bag(' + str(z) + ')'
    def __str__(self):
        string = 'Bag('
        z = []
        for i in self.bag:
            z.append('{}[{}]'.format(i,self.bag[i]))
        if(self.bag != defaultdict(int)):
            return string + str(z) + ')'
        return 'Bag()'
    def __len__(self):
        count = 0
        for i in self.bag:
            count += self.bag[i]
        return count 
    def unique(self):
        count = 0
        for i in self.bag:
            count += 1
        return count
    def __contains__(self,item):
        return item in self.bag 
    def count(self,item):
        if(item in self.bag):
            return self.bag[item]
        return 0
    def add(self,item):

        self.bag[item] += 1
    def __add__(self,right):
        if(type(right) != Bag):
            raise TypeError
        z = Bag()
        for i in right.bag:
            for tok in range(right.bag[i]):
                z.add(i)
        for t in self.bag:
            for zok in range(self.bag[t]):
                z.add(t)
        return z
    def remove(self,item):
        if(item not in self.bag):
            raise ValueError 
        self.bag[item] -= 1
        for i in self.bag:
            if(self.bag[i]== 0):
                del self.bag[i]
                break
    def __eq__(self,right):
        if(type(right) != Bag):
            return self.bag == right
        return self.bag == right.bag 
    def __neq__(self,right):
        if(type(right) != Bag):
            return self.bag != right
        return self.bag != right.bag
    def _gen(bag):
        for i in bag:
            for t in range(bag[i]):
                yield i
    def __iter__(self):


        return Bag._gen(dict(self.bag))
        





if __name__ == '__main__':

    
    #driver tests
    import driver
    driver.default_file_name = 'bsc2.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
