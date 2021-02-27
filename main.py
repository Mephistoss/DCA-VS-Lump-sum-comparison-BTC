import numpy as np
from matplotlib import pyplot as plt

# import csv
#  numpy import genfromtxt

price_data = np.genfromtxt("BNC BLX, 1D.csv", delimiter=",")
column = price_data[1:, 4]
length = len(column)

days = list(range(1, length + 1))
column_list = column.tolist()

print(column)
dim = column.ndim

plt.title("Bitcoin log chart"); plt.ylabel("BTC log price"); plt.xlabel("days")
plt.plot(days, column); plt.yscale("log"); plt.show()
