import numpy as np
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

width = 0.25

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

x_index = np.arange(len(ages_x))

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(x_index, dev_y, width=0.25, color="#444444", label="All Devs")

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(x_index + width, py_dev_y, width=0.25, color="#008fd5", label="Python")

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_index - width, js_dev_y, width=0.25, color="#e5ae38", label="JavaScript")

plt.legend()

plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

plt.tight_layout()
plt.xticks(ticks=x_index,labels=ages_x)
plt.show()