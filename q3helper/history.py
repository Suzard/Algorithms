from collections import defaultdict

#Submitter edwardc6(Chen,Edward)
class History:
    def __init__(self):
        self.history = defaultdict(list)

    def __getattr__(self,name):
        count = 0
        t = name.split('_prev')
        for i in t:
            if(i == ''):
                count += 1
        if(t[0] not in self.__dict__):
            raise NameError
        tount = 0
        for i in self.history:
            tount += 1
        if(tount >= count+1):
            for k in self.history[len(self.history)-count-1]:
                if(k[0] == t[0]):
                    return k[1]
        return None
                
            


    def __getitem__(self,index):
        if(index>0):
            raise IndexError
        t = dict()
        total_variables = set()
        for i in self.history:
            for g in self.history[i]:
                total_variables.add(g[0])
        for var in total_variables:
            count = 0
            for item in sorted(self.history, reverse = True):

                for kor in self.history[item]:
                    if(kor[0] == var):
                        if(count == index):
                            t[var] = kor[1]
                        count -= 1
            if(var not in t):
                t[var] = None
        return t
            

    
    def __setattr__(self,name,value):
        if('_prev' in name):
            raise NameError
        else:
            self.__dict__[name] = value
            count = 0
            toz = []
            for i in self.__dict__:
                if(i != 'history'):
                    toz.append((i,self.__dict__[i]))
            if(len(self.history) > 0):
                for geo in self.history:
                    for teo in self.history[geo]:
                        if(teo[0] == name):
                            count += 1
            for g in toz:
                if(g[0] in [tok[0] for tok in self.history[count]]):
                    pass
                else:
                    self.history.setdefault(count, []).append([g[0], g[1]])
if __name__ == '__main__':
    # Put in simple tests for History before allowing driver to run

    print()
    import driver
    
    driver.default_file_name = 'bsc2.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
