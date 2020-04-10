
import pandas as pd
import numpy as np
from datetime import datetime
import random

start = "20180103 09:00:00"
end = "20180103 15:00:00"
datetime_start = datetime.strptime(start,"%Y%m%d %H:%M:%S")
datetime_end = datetime.strptime(end,"%Y%m%d %H:%M:%S")

a =  pd.date_range(datetime_start,datetime_end,freq='T') 
for i in a:
	print(i)
'''
print(np.random.rand(10))
print(len(a))


symbol_list = list("ABC")
x = np.random.choice(symbol_list, size=10, replace=True)
print(x)
'''