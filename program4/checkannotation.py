from goody import type_as_str
import inspect
import bag
# Submitter: edwardc6(Chen, Edward)
# Partner : cshenk(Shenk, Christian)
#Lab#4
bag_definition = bag.Bag

class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (by raising AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (by raising AssertionError) this classes raises AssertionError and prints
      its failure, along with a list of all annotations tried followed by the
      check_history.
    """
    
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value, check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 



class Check_Annotation():
    # set name to True for checking to occur
    checking_on  = True
  
    # self._checking_on must also be true for checking to occur
    def __init__(self,f):
        self._f = f
        self.checking_on = True
        self.jk  = dict()
        
    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)
        def ultimate_function(self,param,annot,value):
            if(type(value) != type(annot)):
                raise AssertionError('value does not match annot')
            count = 0

            for i in annot:
                try:

                    if(type(i) == tuple or type(i) == dict or type(i) == list
                      or type(i) == set or type(i) == frozenset):
                        if(len(annot) != 1):
                            self.check(param, value[count],i)
                        if(len(annot) == 1):
                           
                            
                            for talk in value[count:]:
                                    self.check(param, i, talk)
                    elif(inspect.isfunction(i) == True):
                        if(type(value) == list or 
                           type(value) == set or
                           type(value) == frozenset):
                            for t in value:
                                if(i(t) == False):
                                    raise AssertionError('value does not match annot')
                        else:

                            if(i(value) == False):

                                raise AssertionError('value does not match annot')


                    else:
                        try:
                            if(isinstance(value[count],i) != True):
                                raise AssertionError('value does not match annot')
                            if(len(annot) == 1):
                                if(len(value[count:]) >= 1):
                                    for jk in value[count:]:
                                        if(isinstance(jk,i) != True):
                                            raise AssertionError('value does not match annot')
                        except:
                            raise AssertionError('value does not match annot')
                    
                    count += 1
  


                except:
                    raise AssertionError('value does not match annot')
        def sets(self,param,annot,value):
            if(type(value) != type(annot)):
                raise AssertionError('value does not match annot')
            if(len(annot) != 1):
                raise AssertionError('value does not match annot')
            for jk in annot:
                pass
            for i in value:
                if(isinstance(i, jk) != True):
                    raise AssertionError('value does not match annot')
                            
            
            
        # Decode the annotation and check it 

        
        if(isinstance(annot,type)):
            if(isinstance(value, annot) != True):
                
                raise AssertionError('value does not match annot')
        elif(isinstance(annot,list)):

            ultimate_function(self, param,annot,value)

            
        elif(isinstance(annot, tuple)):
            ultimate_function(self, param,annot,value)

        elif(isinstance(annot, dict)):
            if(type(value) != type(annot)):
                raise AssertionError('value does not match annot')
            z = []
            for t in value:
                z.append((t,value[t]))
            zook = []
            took = []
            for g in z:
                zook.append(g[0])
                took.append(g[1])
                
            count = 0
            try:
                for i in annot:
                    if(annot[i] == tuple or annot[i] == dict or annot[i] == list
                      or annot[i] == set or annot[i] == frozenset):
                        for kook in took:
                            
                            ultimate_function(self, param,annot[i],value)

                        
                            
                    else:
                        for zok in zook:
                            if(isinstance(zok, i) != True):
                    
                                raise AssertionError('value does not match annot')
                            
                        for jok in took:
                            if(isinstance(jok, annot[i]) != True):
                    
                                raise AssertionError('value does not match annot')


            except:
                
                raise AssertionError
            

                
        elif(isinstance(annot, set)):
            sets(self,param,annot,value)
                
        elif(isinstance(annot, frozenset)):
            sets(self,param,annot,value)
        elif (inspect.isfunction(annot) == True):
            if(len(annot.__code__.co_varnames) != 1):
                raise AssertionError('value does not match annot')
            try:
                if(annot(value) == False):
                    raise AssertionError('value does not match annot')
            except:
                raise AssertionError('value does not match annot')
        elif(isinstance(annot,str)):
            try:
                if(annot not in self.jk):
                    juke = []
                    juke.append(value)
                    self.jk[annot] = juke
                else:
                    juke.append(value)
                    self.jk[annot]  = juke
                


                toz = []

                for i in param:
                    toz.append(str(i))
                k = ','.join(toz)
                for tuze in self.jk[annot]:
                    pass
                
                if(len(toz) > 1):
                    jiz = []
                    for tk in value:
                        jiz.append(tk)
                    zok = ','.join(jiz)
                    z = eval('lambda {}:{}'.format(k,annot))
                    if(z(eval(zok)) == False):
                        raise AssertionError('value does not match annot')
                    

                        
                else:
                            
                            
                    z = eval('lambda {}:{}'.format(k,annot))
                        
                        
                    if(z(value) == False):
                        raise AssertionError('value does not match annot')
            except:
                raise AssertionError('value does not match annot')
        else:
            try:
                annot.__check_annotation__(self,param,annot,value)
                g = eval(annot)
                toz = []
                for i in param:
                    toz.append(str(i))
                k = ','.join(toz)
                    
                    
                z = eval('lambda {}:{}'.format(k,g))
                
                
                if(z(value) == False):
                    raise AssertionError('value does not match annot')
            except:
                

                raise AssertionError('value does not match annot')
        
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):
        
        # Return a dictionary of the parameter/argument bindings (actually an
        #    ordereddict, in the order parameters occur in the function's header)
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if param.name not in bound_f_signature.arguments:
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments
        if(self.checking_on != True):
            return self._f(*args,**kargs)
        
        # On first AssertionError, print the source lines of the function and reraise 
        g = param_arg_bindings()
        s = self._f.__annotations__
        for i in g:
            if(s.get(i) != None):
                self.check(i,s.get(i),g.get(i))
        if(s.get('return') != None):
            g.update({'_return':self._f(*args,**kargs)})
            self.check('return', s.get('return'), g.get('_return'))
        else:
            pass 
            
        return self._f(*args,**kargs)
        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        
#         try:
#             # Check the annotation for every parameter (if there is one)
#                     
#             # Compute/remember the value of the decorated function
#             
#             # If 'return' is in the annotation, check it
#             
#             # Return the decorated answer
#             
#             pass #remove after adding real code in try/except
#             
#         # On first AssertionError, print the source lines of the function and reraise 
#         except AssertionError:
#             print(80*'-')
#             for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
#                 print(l.rstrip())
#             print(80*'-')
#             raise




  
if __name__ == '__main__':     

           
    import driver
    driver.driver()
