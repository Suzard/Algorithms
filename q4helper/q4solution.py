# primes is used to test code you write below
from predicate import is_prime

def primes(max=None):
    p = 2
    while max == None or p <= max:
        if is_prime(p):
            yield p
        p += 1 

# Generators must be able to iterate through any iterable.
# hide is present and called to ensure that your generator code works on
#   general iterable parameters (not just a string, list, etc.)
# For example, although we can call len(string) we cannot call
#   len(hide(string)), so the generator functions you write should not
#   call len on any parameters
# Leave hide in this file and add code for the other generators.

def hide(iterable):
    for v in iterable:
        yield v


def peaks(iterable):
    z = iter(iterable)
    present = next(z)
    future = present
    t = []
    while z:
        try:
            prev = present 
            present = future 
            future = next(z)
            if(present>prev and present>future):
                t.append(present)
        except StopIteration:
            break
    return t
        
         
 
 
def compress(vit,bit): 
    t = zip(vit,bit)
    for g,v in t:
        if(v):
            yield g

            
def stop_when(iterable,p):
    for i in iterable:
        if(p(i)):
            break
        yield i
   
                       
def start_when(iterable,p):
    for i in iterable:
        if(p(i)):
            yield i 
            iterable = i
            

def alternate(*args):
    z = [iter(i) for i in args]
    while z:
        for i in z:
            yield next(i)


class Ordered:
    def __init__(self,aset):
        self.aset = aset

    def __iter__(self):
        try:
            mini = min(self.aset)
            yield mini
    
            while self.aset:
                calculate_min = [i for i in self.aset if i>mini]
                if not calculate_min:
                    return 
                else:
                    mini = min(calculate_min)
                    yield mini
        except ValueError:
            raise StopIteration




if __name__ == '__main__':
    from goody import irange
    
    # Test peaks; add your own test cases
#     print('Testing peaks')
#     print(peaks([0,1,-1,3,8,4,3,5,4,3,8]))
#     print(peaks([5,2,4,9,6,1,3,8,0,7]))
#     print(peaks([1,2,3,4,5]))
#     print(peaks([0,1]))
    
    #prints a 1 for every prime preceded/followed by a non prime
    #below 5, 7, 11, 13, 17, 19 have that property the result should be a list of 6 1s
    #[1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20]
    #[0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
#     print(list(int(is_prime(p)) for p in irange(1,20)))
#     print(peaks(int(is_prime(p)) for p in irange(1,20)))
#     
#     
#     # Test compress; add your own test cases
#     print('\nTesting compress')
#     for i in compress('abcdefghijklmnopqrstuvwxyz',
#                       [is_prime(i) for i in irange(1,26)]):
#         print(i,end='')
#     print()

#     for i in compress('abcdefghijklmnopqrstuvwxyz',
#                       (is_prime(i) for i in irange(1,26))):
#         print(i,end='')
#     print('\n')
#     
#     
#     # Test stop_when; add your own test cases
#     print('\nTesting stop_when')
#     for c in stop_when('abcdefghijk', lambda x : x >='d'):
#         print(c,end='')
#     print()
# 
#     for c in stop_when(hide('abcdefghijk'), lambda x : x >='d'):
#         print(c,end='')
#     print('\n')
# 
#    
#     # Test start_when; add your own test cases
#     print('\nTesting start_when')
#     for c in start_when(hide('abcdefghijk'), lambda x : x >='d'):
#         print(c,end='')
#     print()
# 
#     for c in start_when(hide('abcdefghijk'), lambda x : x >='d'):
#         print(c,end='')
#     print('\n')
# 
#               
#     # Test alternate; add your own test cases
#     print('\nTesting alternate')
#     for i in alternate('abcde','fg','hijk'):
#         print(i,end='')
#     print()
#        
#     for i in alternate(hide('abcde'), hide('fg'),hide('hijk')):
#         print(i,end='')
#     print()
#        
#     for i in alternate(primes(20), hide('fghi'),hide('jk')):
#         print(i,end='')
#     print('\n')
#        
#     
#     # Test Ordered; add your own test cases
#     print('\nTesting Ordered')
#     s = {1, 2, 4, 8, 16}
#     i = iter(Ordered(s))
#     print(next(i))
#     print(next(i))
#     s.remove(8)
#     print(next(i))
#     print(next(i))
#     s.add(32)
#     print(next(i))
#     print()
#    
#     s = {1, 2, 4, 8, 16}
#     i = iter(Ordered(s))
#     print([next(i), next(i), s.remove(8), next(i), next(i), s.add(32), next(i)])
#     
#     s = {1, 2, 4, 8}
#     for v in Ordered(s):
#         s.discard(8)
#         s.add(10)
#         print(v) 
#     print('\n')
#          
#          
    import driver
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
    
