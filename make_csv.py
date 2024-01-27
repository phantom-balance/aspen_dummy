"make_csv.py"

import numpy as np
import pandas as pd

def make_csv(X_val, Y_val, column_lab, file_name="data.csv"):
    X_arr = np.array(X_val)
    Y_arr = np.array(Y_val)
    data_arr = np.hstack((X_arr, Y_arr))
    df = pd.DataFrame(data_arr, columns=column_lab)
    print(f"Saving the data == DATA/{file_name}")
    df.to_csv(f"DATA/{file_name}", index=False)

# columns_lab = ["a", "b", "c"]
# X_val = [[1,2],[3,4],[5,6],[7,8],[9, 10]]
# Y_val = [[1], [2], [3], [44], [99]]
# make_csv(X_val, Y_val,column_lab=columns_lab, file_name="data.csv")