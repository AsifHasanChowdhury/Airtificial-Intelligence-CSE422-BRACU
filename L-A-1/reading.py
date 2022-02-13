import queue
import numpy as dp
work="F:\\CSE422\\New folder\\work2.txt"

array_from_file = dp.loadtxt(work, dtype=dp.chararray, skiprows=2)

print(array_from_file)