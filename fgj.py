import numpy as np
import pandas as pd
from sklearn.decomposition import PCA


def correlation(dataset, threshold):
    col_corr = set()
    corr_matrix = dataset.corr()
    i = dataset.columns.get_loc("Effort")
    for j in range(len(corr_matrix.columns)):
        if i == j:
            continue
        if abs(corr_matrix.iloc[i, j]) <= threshold:
            colname = corr_matrix.columns[j]
            col_corr.add(colname)
            del dataset[colname]
    #print(col_corr)
    print(dataset)
    print(corr_matrix)

f = open('dataset.txt', "r")
content = f.readlines()

data = []
for line in content:
    line = line.strip("\n").split(",")
    each_list = []
    for i, num in enumerate(line):
        if i != 0:
            if num != "?":
                each_list.append(int(num))
            else:
                each_list.append(-1)
    data.append(each_list)
data = np.array(data)

mean_array = np.zeros(data.shape[1])

for i in range(data.shape[1]):
    k = 0.0
    for j in range(data.shape[0]):
        if data[j][i] != -1:
            mean_array[i] += data[j][i]
            k += 1
    mean_array[i] /= k
    for j in range(data.shape[0]):
        if data[j][i] == -1:
            data[j][i] = mean_array[i]


C = pd.Index(["TeamExp", "ManagerExp", "YearEnd", "Length", "Effort", "Transactions", "Entities", "PointsAdjust",
                "Envergure", "PointsNonAjust", "Langage"], name="cols")
df = pd.DataFrame(data=data,
                  columns=C)
correlation(df, 0.8)

g = open('diffcorr_dataset.txt', "a+")
df.to_csv(g, sep=',', index=False)
"""
pca = PCA(n_components=5)
data = pca.fit_transform(data)

print(data)
#no change in code
"""
