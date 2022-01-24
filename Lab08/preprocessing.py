#my preprocessing script
#not exactly legal, but that's why you don't have to run it lol

#it works ok


import pandas as pd
import numpy as np

a = np.array(pd.read_csv("~/Downloads/Astros.tsv", sep='\t'))
b = np.array(pd.read_csv("~/Downloads/Braves.tsv", sep='\t'))

with (open('_astros.data', 'w') as astros,
      open('_braves.data', 'w') as braves):
    print(repr(a), file=astros)
    print(repr(b), file=braves)
