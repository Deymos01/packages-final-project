import sys

import pandas as pd

dataframe = pd.read_excel('.\\data\\финальные_данные.xlsx')

blarr = dataframe["Ther"].str.contains("среднетяжелое течение")
groupA = dataframe[blarr]
groupB = dataframe[~blarr]

resDgroupA = groupA["Результат_D"].apply(lambda x: isinstance(x, float) or isinstance(x, int))
resDgroupB = groupB["Результат_D"].apply(lambda x: isinstance(x, float) or isinstance(x, int))

resFgroupA = groupA["Результат_F"].apply(lambda x: isinstance(x, float) or isinstance(x, int))
resFgroupB = groupB["Результат_F"].apply(lambda x: isinstance(x, float) or isinstance(x, int))

for indexA, rowA in groupA.iterrows():
    for indexB, rowB in groupB.iterrows():
        if (rowA["Gender"] == rowB["Gender"] and
            abs(rowA["Age"] - rowB["Age"]) <= 3 and
            resDgroupA[indexA] and resDgroupB[indexB] and
            abs(rowA["Результат_D"] - rowB["Результат_D"]) / rowA["Результат_D"] <= 0.1 and
            resFgroupA[indexA] and resFgroupB[indexB] and
            abs(rowA["Результат_F"] - rowB["Результат_F"]) / rowA["Результат_F"] <= 0.1):
            pass



