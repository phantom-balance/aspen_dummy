import numpy as np 

class aspen:
    def __init__(self, path):
        self.path = path
    
    def func(self, x):
        # y1 = np.sqrt(np.absolute(np.sin(np.sqrt(np.absolute(x[0]**2+x[1]**2)))))+0.01*(x[0]+x[1])
        y1 = -x[0]*x[1]*(72-2*x[0]-2*x[1])
        y2 = 2*x[0]+3*x[1]-2

        y = [y1, y2]

        return y
    
    def single_play(self,  X_val, X_node=None, Y_node=None):
        Y_val = self.func(X_val)
        return X_val, Y_val

    def sampling(self, X_val, X_node=None, Y_node=None):
        Y_val = []
        for i in range(len(X_val)):
            temp_Y = self.func(X_val[i])
            Y_val.append(temp_Y)
        
        return X_val, Y_val


file_name="002_recreate.bkp"
sim=aspen(path=file_name)  
# X_val = [1, 1]
# x, y = sim.single_play(X_val=X_val)
# print(x, y)
from sampling import grid_sample, latin_hypercube_sample

bounds = {"x1":[0,5], "x2":[0,5]}
X_val = grid_sample(bounds, num_samples=10)
print(X_val)
X_val = latin_hypercube_sample(bounds, num_samples=10, seed=42)
print(X_val)

x, y = sim.sampling(X_val)


'''
import os
import numpy as np
import torch
import win32com.client as win32

class aspen:
    def __init__(self, path):
        self.path = path
        self.Application = win32.gencache.EnsureDispatch("Apwn.Document")
        self.Application.InitFromArchive2(os.path.abspath(path))
        
    def start_up(self):
        self.Application = win32.gencache.EnsureDispatch("Apwn.Document")
        self.Application.InitFromArchive2(os.path.abspath(self.path))
        self.Application.Engine.Run2()

    def close(self):
        self.Application.Close(os.path.abspath(self.path))

    def Reinit(self):
        self.Application.Reinit()
      
    def print_val(self, nodes):
        for i in range(len(nodes)):
            print(self.Application.Tree.FindNode(nodes[i]).Value)

    def single_play(self,X_node, Y_node, X_val):
        # self.Application.Engine.Run2()
        Y_val=[]
        for i in range(len(X_node)):
            self.Application.Tree.FindNode(X_node[i]).Value=X_val[i]

        self.Application.Engine.Run2()
        for i in range(len(Y_node)):
            Y_val.append(self.Application.Tree.FindNode(Y_node[i]).Value)

        return X_val, Y_val
    def sampling(self, X_node, Y_node, X_val):
        Y_val=[]
        for i in range(len(X_val)):
            for j in range(len(X_node)):
                self.Application.Tree.FindNode(X_node[i]).Value=X_val[i][j]
            self.Application.Engine.Run2()
            temp_Y = []
            for k in range(len(Y_node)):
                temp_Y.append(self.Application.Tree.FindNode(Y_node[i]).Value)
            Y_val.append(temp_Y)
            
        return X_val, Y_val
    
# file_name="002_recreate.bkp"
# sim=aspen(path=file_name)

'''