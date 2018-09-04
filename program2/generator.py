# Generators must be able to iterate through any iterable.
# hide is present and called to ensure that your generator code works on
#   general iterable parameters (not just on a string, tuple, list, etc.)
# For example, although we can call len(string) we cannot call
#   len(hide(string)), so the generator functions you write should not
#   call len on their parameters
# Leave hide in this file and add code for the other generators.

def hide(iterable):
    for v in iterable:
        yield v


def running_count(iterable,p):
    count = 0
    for i in iterable:
        if(p(i)):
            count += 1
        yield count

        
def n_with_pad(iterable,n,pad=None):
    z= iter(iterable)
    for i in range(n):
        try:
            yield next(z)
        except StopIteration:
            yield pad

        

    


def overlap(iterable,n,m=1):
    t = iter(iterable)
    z = [next(t) for i in range(n)]
    while t:
        try:
            yield z
            lo = [next(t) for z in range(m)]
            z = z[m:] + lo
            
            
        except StopIteration:
            break

def yield_and_skip(iterable):
    z = iter(iterable)
    while z:
        try:
            p = next(z)
            yield p
            if(type(p) == int):
                for i in range(p):
                    next(z)
        except StopIteration:
            break
        
def skip_bad_and_next(iterable,p): # predicate p(n) true if n is good
    t= iter(iterable)
    present= next(t)
    future = present

    while t:
        try:
                    
            past = present
            present = future 
            if(p(present)== True and p(past)== True):
                yield present 
            future = next(t)

        except StopIteration:

            break

def alternate(*args):

    z = [iter(i) for i in args]
    while z:
        count = 0
        for i in z:
            count += 1
            try:
                yield next(i)
            except:
                z.remove(z[count-1])
                z = z[count-1:] + z[:count-1]
                continue
                
            

            
        





if __name__ == '__main__':
#     print('\nTesting running_count')
#     for i in running_count('bananastand',lambda x : x in 'aeiou'): # is vowel
#         print(i,end=' ')
#     print()
#     for i in running_count(hide('bananastand'),lambda x : x in 'aeiou'): # is vowel
#         print(i,end=' ')
#     print()
#     
# 
#     print('\nTesting n_with_pad')
#     for i in n_with_pad('abcdefg',3,None):
#         print(i,end=' ')
#     print()
#     for i in n_with_pad(hide('abcdefg'),3,None):
#         print(i,end=' ')
#     print()
#     for i in n_with_pad(hide('abcdefg'),10):
#         print(i,end=' ')
#     print()
#     for i in n_with_pad(hide('abcdefg'),10,'?'):
#         print(i,end=' ')
#     print()
#     for i in n_with_pad(hide('abcdefg'),10):
#         print(i,end=' ')
#     print()
#     
#      
#     print('\nTesting overlap')
#     for i in overlap('abcdefghijk',3,2):
#         print(i,end=' ')
#     print()
#     for i in overlap(hide('abcdefghijk'),3,2):
#         print(i,end=' ')
#     print()
#     
#     
#     print('\nTesting yield_and_skip')
#     for i in yield_and_skip([1, 2, 1, 3, 'a', 'b', 2, 5, 'c', 1, 2, 3, 8, 'x', 'y', 'z', 2]):
#         print(i,end=' ')
#     print()
#     for i in yield_and_skip(hide([1, 2, 1, 3, 'a', 'b', 2, 5, 'c', 1, 2, 3, 8, 'x', 'y', 'z', 2])):
#         print(i,end=' ')
#     print()
#     
#     
#     print('\nTesting skip_bad_and_next')
#     for i in skip_bad_and_next('abxcdxxefxgxxxxxxxabc',lambda x: x != 'x'):
#         print(i,end=' ')
#     print()
#     for i in skip_bad_and_next(hide('abxcdxxefxgxxxxxxxabc'),lambda x: x != 'x'):
#         print(i,end=' ')
#     print()
#     
#     
#     print('\nTesting alternate')
#     for i in alternate('abcde','fg','hijk'):
#         print(i,end=' ')
#     print()
#     for i in alternate(hide('abcde'),hide('fg'),hide('hijk')):
#         print(i,end=' ')
#     print()
#     
#     
#     print()
    #driver tests
    import driver
    driver.default_file_name = 'bsc3.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
