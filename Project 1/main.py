import statistics
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from util import extractListFromMatrixX, zipLists


df = pd.read_excel("./adsl.xlsx")

fig, ax = plt.subplots()

ax.axis("off")

data_points = ["AGE", "BMI", "HEIGHT", "WEIGHT"]

rows = []

data = []

for i in range(len(df.index)):
    c = []

    for data_point in data_points:
        c.append(df[data_point][i])

    data.append(c)

n = ["n"]
mean = ["mean"]
median = ["median"]
sd = ["SD"]
_min = ["Min"]
_max = ["Max"]

for index, name in enumerate(data_points):
    d = extractListFromMatrixX(data, index)

    n.append(len(d))
    mean.append(round(sum(d) / len(d), 2))
    median.append(round(statistics.median(d), 2))
    sd.append(round(statistics.stdev(d), 2))
    _min.append(min(d))
    _max.append(max(d))

rows = zipLists(n, mean, median, sd, _min, _max)

table = ax.table(cellText=rows, colLabels=["statistic", *data_points], loc="center", cellLoc="center")

table.auto_set_font_size(False)

plt.savefig("output.png")
plt.show()