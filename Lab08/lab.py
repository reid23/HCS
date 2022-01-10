import pandas as pd
import numpy as np

a = np.array(pd.read_csv("~/Downloads/Astros.tsv", sep='\t'))
b = np.array(pd.read_csv("~/Downloads/Braves.tsv", sep='\t'))

print(repr(a))
print(repr(b))
