import numpy as np
from typing import List

csv_file:str = "./file.csv"
read_file = np.loadtxt(csv_file)


position:List = []

for i in range(len(read_file)):
    x = read_file[i][0]
    y = read_file[i][1]
    timestamp = read_file[i][2]

    position.append([x, y, timestamp])

print(position)







