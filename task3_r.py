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

res = pd.DataFrame(columns=["CaseID_A", "CaseID_B", "Age_A", "Age_B", "Gender", "Result_D_A", "Result_D_B", "Result_F_A", "Result_F_B"])

for indexA, rowA in groupA.iterrows():
    print(indexA)
    for indexB, rowB in groupB.iterrows():
        if (rowA["Gender"] == rowB["Gender"] and
                abs(rowA["Age"] - rowB["Age"]) <= 3 and
                resDgroupA[indexA] and resDgroupB[indexB] and
                abs(rowA["Результат_D"] - rowB["Результат_D"]) / rowA["Результат_D"] <= 0.1 and
                resFgroupA[indexA] and resFgroupB[indexB] and
                abs(rowA["Результат_F"] - rowB["Результат_F"]) / rowA["Результат_F"] <= 0.1):
            res = res._append({"CaseID_A": rowA["CaseID"], "CaseID_B": rowB["CaseID"],
                               "Age_A": rowA["Age"], "Age_B": rowB["Age"], "Gender": rowA["Gender"],
                               "Result_D_A": rowA["Результат_D"], "Result_D_B": rowB["Результат_D"],
                               "Result_F_A": rowA["Результат_F"], "Result_F_B": rowB["Результат_F"]}, ignore_index=True)

res.to_excel('.\\data\\результаты.xlsx', index=False)
