import unittest  # use unittest.TestCase
from graph import Graph, GraphError
#Submitter edwardc6(Chen,Edward)

class Test_Graph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph(('a','b',1), ('a','c',3),
             ('b','a',2), ('d','b',2), ('d','c',1),'e')
    def test_del1(self):
        count = 0
        for i in self.graph:
            if(len(i) == 3):
                count += 1
        self.assertEqual(5,count)
        z = self.graph 
        for t in z:
            if(len(t) == 3):
                del self.graph[t[0],t[1]]
                count -= 1
            self.assertEqual(len(self.graph), count)
    def test_del2(self):
        count = 0
        tz = []
        for i in self.graph:
            
            if(len(i) == 3):
                if(i[0] not in tz):
                    tz.append(i[0])
                if(i[1] not in tz):
                    tz.append(i[1])
                count += 1
            elif(len(i) == 1):
                tz.append(i)
        self.assertEqual(5,count)
        gok = sorted(tz, reverse = True)
        z = self.graph 
        for g in gok:
            for t in z:
                if(len(t) == 3):
                    
                    if(g in t):
                        
                        del self.graph[t[0],t[1]]
                        count -= 1
                        
                            
                elif(len(t) == 1):
                    if(t == g):
                        del self.graph[t]
                    
            self.assertEqual(len(self.graph), count)
    def test_del3(self):
        self.assertRaises(GraphError, self.graph.__delitem__ ,1)
        self.assertRaises(GraphError, self.graph.__delitem__ ,('a','b',1,1))
        self.assertRaises(GraphError, self.graph.__delitem__ ,(2,'b'))
        self.assertRaises(GraphError, self.graph.__delitem__ ,('b',1))

        pass 
    def test_in(self):
        z = []
        for i in self.graph:
            if(len(i) == 1):
                z.append(i)
            else: 
                for kog in i:
                    z.append(kog)
                    
        for g in self.graph:
            if(len(g) == 1):
                self.assertIn(g,self.graph)
            else:
                self.assertIn(g,self.graph)
                self.assertIn(g[0], z)
                self.assertIn(g[1], z)
        self.assertNotIn('y',self.graph)
        self.assertNotin(('c','a'), self.graph)
        self.assertNotin(('a','c',4), self.graph)
                
            
    def test_degree(self):
        z = ['a','b','c','d','e']
        g = dict()
        for i in z:
            g[i] = self.graph.degree(i)
        #comment this out if you want no errors
        self.assertDictEqual(g,{'a':3, 'b':3, 'c':2, 'd':2 , 'e':0})

        
        
              
         
