import re, traceback, keyword
#Submitter: edwardc6(Chen, Edward)
# Partner : cshenk(Shenk, Christian)
#Lab#4


def pnamedtuple(type_name, field_names, mutable=False):
    def del_space(something):
        h = something.split(',')
        j = []
        for i in h:
            i = i.replace(' ', '')
            j.append(i)
        return j
    def create_initializing(var_list):
        g = ''
        for i in var_list:
            g += 'self.{},'.format(i)
        g = g[0:-1]
        g += ' ='
        for t in var_list:
            g += '{},'.format(t)
        g = g[0:-1]
        return g

    def repr_initializing(z,var_list):
        g = "'" +z + '('
        for i in var_list:
            g += '{zood}={{{zood}}},'.format(zood= i)
        g  = g[0:-1]
        g += ")'.format("
        for t in var_list:
            g += '{kood}=self.{kood},'.format(kood =t)
        g = g[0:-1]
        g+= ')'
        return g
    def get_functions(var_list):
        z = ''
        for i in var_list:
            z += '    def get_{dude}(self):\n'.format(dude = i)
            z += '        return self.{zude}'.format(zude = i)
            z += '\n'
        return z

    def zog(string):
        z = string.split('(self)')
        june = []
        for i in z:
            count = 0
            k = i.find('get_') +4
            if(k != 3):
                juke = 'self.get_{}()'.format(i[k:])
                june.append((i[k:],juke))
        return june

    def legal_name_ver(k):
        legal_name = '^([a-zA-Z][\_a-zA-Z0-9]*)$'
        if(type(k) != str):
            raise SyntaxError('The names are not legal')
        if(re.match(legal_name,k) == None):
            return False
        if(re.match(legal_name,k) != None):
            for i in keyword.kwlist:
            
                if(i == k):
                    return False
            return True
        
    def show_listing(s):
        for i, l in enumerate(s.split('\n'),1):
            print('{num: >3} {txt}'.format(num = i, txt = l.rstrip()))
            
    if(type(type_name) != str):
        raise SyntaxError('type_name is not legal type')
    if(legal_name_ver(type_name) == False):
        raise SyntaxError('type_name did not fit conditions')
    if(type(field_names) == str):
        if(',' not in field_names):
            a = field_names.split()
            for i in a:
                if(legal_name_ver(i) == False):
                    raise SyntaxError('one of the field names did not fit conditions')
            field_names = a
        else:
            a = del_space(field_names)
            field_names = a
    if(type(field_names) == list):
        for i in field_names:
            if(legal_name_ver(i) == False):
                raise SyntaxError('one of the field names did not fit conditions')
    if(type(field_names) != str and type(field_names) != list):
        raise SyntaxError('The type of the field names did not fit conditions')

    class_template  =  '''\
class {type_name}:
    def __init__(self, {fields}):
        {initializing}
        self._fields = {fields_list}
        self._mutable = {mutable} 
        self.g = {type_name}
        
    def __repr__(self):
        return {returning}
    
{get_functions}

    def __getitem__(self,g):
        if(type(g) == int):
            if(len(self._fields)<g):
                raise IndexError('Out of bounds int')
            z = self._fields[g]
            for i in {zog}:
                if(i[0] == z):
                    return eval(i[1])
                    

        elif(type(g) == str):
            if(g in self._fields):
                for i in {zog}:
                    if(i[0] == g):
                        return eval(i[1])
            else:
                raise IndexError('Out of bounds in self._fields')
                
        else:
            raise IndexError('Not valid typing')

    def __eq__(self,right):
        if(self._fields != right._fields or self.g != right.g):
            return False
        for i in self._fields:
            if(i not in right._fields):
                return False
            if(self[i] != right[i]):
                return False
        for t in right._fields:
            if(t not in self._fields):
                return False
            if(self[t] != right[t]):
                return False
        return True
    def _replace(self, **kargs):
        for i in kargs:
            if(str(i) not in self._fields):
                raise TypeError('value not in self._fields')
        if self._mutable == True:
            for i in kargs:
                self.__dict__[i] = kargs[i]
                
            return None
        else:
            z = eval(repr(self))
            for j in kargs:
                z.__dict__[j] = kargs[j]
            return z
            
    def __setattr__(self,j, v):
        if(j in self.__dict__ and self._mutable == False):
            raise AttributeError('mutable is false and value j is not in self.dict')
        else:
            self.__dict__[j] = v
'''
    class_definition = class_template.format(type_name = type_name, 
                                             initializing = create_initializing(field_names),
                                             fields_list = field_names,
                                             fields = ','.join(field_names), mutable = mutable,
                                             returning = repr_initializing(type_name,field_names),
                                             get_functions = get_functions(field_names), zog = zog(get_functions(field_names))
                                             )
    name_space = dict(__name__='pnamedtuple_{type_name}'.format(type_name=type_name))
    try:
        exec(class_definition, name_space)
        name_space[type_name].source_code = class_definition
    except(SyntaxError, TypeError):
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]
    
if __name__ == '__main__':
    import driver
    driver.driver()
