"sampling.py"

import pandas as pd
import numpy as np
from scipy.stats import qmc
from sklearn.model_selection import ParameterGrid

def grid_sample(bounds, num_samples):
    grid = {}
    num_pts_per_dim = max(1, np.floor(num_samples**(1/len(bounds))).astype(int))
    for name, bnd in bounds.items():
        grid[name] = np.linspace(bnd[0], bnd[1], num=num_pts_per_dim)
        
    df = pd.DataFrame(list(ParameterGrid(grid)))
    sample = df.values.tolist()
    return sample

def latin_hypercube_sample(bounds, num_samples=10, seed = None):
    # sampler = qmc.LatinHypercube(d=len(bounds), optimization="random-cd", seed=seed)
    sampler = qmc.LatinHypercube(d=len(bounds), seed=seed)
    samples = sampler.random(num_samples)
    l_bounds = [bound[0] for bound in bounds.values()]
    u_bounds = [bound[1] for bound in bounds.values()]
    samples = qmc.scale(samples, l_bounds, u_bounds)
    return samples

# bounds = {"x1":[0,1], "x2":[0,1]}
# sample = latin_hypercube_sample(bounds, num_samples=10, seed=42) 
# sample = grid_sample(bounds, num_samples=10)