

import pandas as pd
import src.robustness as rb

frame = pd.read_csv('Time_Series_Metrics.csv')

print(list(rb.until( frame['Host 1 Distance traveled until current frame [m]'], (0,100), frame['Host 1 Distance traveled until current frame [m]'])))
