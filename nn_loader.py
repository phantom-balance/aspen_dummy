"nn_loader.py"
import os
import pandas as pd
import torch
from torch.utils.data import Dataset

class loader(Dataset):
    def __init__(self, csv_file, transform=None):
        self.data = torch.tensor(pd.read_csv(csv_file).values)
    def __len__(self):
        return len(self.data)
    def __getitem__(self, index):
        X=self.data[:,:-2][index]
        Y=self.data[:,-2:][index]
        return (X, Y)