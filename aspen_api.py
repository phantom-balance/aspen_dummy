import numpy as np 

class aspen:
    def __init__(self, path):
        self.path = path
    
    def func(self, x):
        y1 = np.sqrt(np.absolute(np.sin(np.sqrt(np.absolute(x[0]**2+x[1]**2)))))+0.01*(x[0]+x[1])
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