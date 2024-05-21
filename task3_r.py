import pandas as pd

dataframe = pd.read_excel('.\\data\\финальные_данные.xlsx')

blarr = dataframe["Ther"].str.contains("среднетяжелое течение")
groupA = dataframe[blarr]
groupB = dataframe[~blarr]

resDgroupA = groupA["Результат_D"].apply(lambda x: isinstance(x, float) or isinstance(x, int))
resDgroupB = groupB["Результат_D"].apply(lambda x: isinstance(x, float) or isinstance(x, int))

resFgroupA = groupA["Результат_F"].apply(lambda x: isinstance(x, float) or isinstance(x, int))
resFgroupB = groupB["Результат_F"].apply(lambda x: isinstance(x, float) or isinstance(x, int))

resGroupA = pd.DataFrame(columns=["CaseID", "Start", "End", "Gender", "Age", "Ther", "Outcome", "Vac", "isMono", "Result_D", "Result_F"])
resGroupB = pd.DataFrame(columns=["CaseID", "Start", "End", "Gender", "Age", "Ther", "Outcome", "Vac", "isMono", "Result_D", "Result_F"])
resGroupC = pd.DataFrame(columns=["CaseID", "Start", "End", "Gender", "Age", "Ther", "Outcome", "Vac", "isMono", "Result_D", "Result_F"])
resGroupD = pd.DataFrame(columns=["CaseID", "Start", "End", "Gender", "Age", "Ther", "Outcome", "Vac", "isMono", "Result_D", "Result_F"])

for indexA, rowA in groupA.iterrows():
    if indexA % 100 == 0: print(f"GroupA: {indexA}")
    if not resDgroupA[indexA] or not resFgroupA[indexA] or pd.isna(rowA["Результат_D"]):
        resGroupC = resGroupC._append({
        "CaseID": rowA["CaseID"],
        "Start": rowA["Start"],
        "End": rowA["End"],
        "Gender": rowA["Gender"],
        "Age": rowA["Age"],
        "Ther": rowA["Ther"],
        "Outcome": rowA["Outcome"],
        "Vac": rowA["Vac"],
        "isMono": rowA["isMono"],
        "Result_D": rowA["Результат_D"],
        "Result_F": rowA["Результат_F"]
    }, ignore_index=True)
        continue
    resGroupA = resGroupA._append({
        "CaseID": rowA["CaseID"],
        "Start": rowA["Start"],
        "End": rowA["End"],
        "Gender": rowA["Gender"],
        "Age": rowA["Age"],
        "Ther": rowA["Ther"],
        "Outcome": rowA["Outcome"],
        "Vac": rowA["Vac"],
        "isMono": rowA["isMono"],
        "Result_D": rowA["Результат_D"],
        "Result_F": rowA["Результат_F"]
    }, ignore_index=True)

for indexB, rowB in groupB.iterrows():
    if indexB % 100 == 0: print(f"GroupB: {indexB}")
    if not resDgroupB[indexB] or not resFgroupB[indexB] or pd.isna(rowB["Результат_D"]):
        resGroupD = resGroupD._append({
        "CaseID": rowB["CaseID"],
        "Start": rowB["Start"],
        "End": rowB["End"],
        "Gender": rowB["Gender"],
        "Age": rowB["Age"],
        "Ther": rowB["Ther"],
        "Outcome": rowB["Outcome"],
        "Vac": rowB["Vac"],
        "isMono": rowB["isMono"],
        "Result_D": rowB["Результат_D"],
        "Result_F": rowB["Результат_F"]
    }, ignore_index=True)
        continue
    resGroupB = resGroupB._append({
        "CaseID": rowB["CaseID"],
        "Start": rowB["Start"],
        "End": rowB["End"],
        "Gender": rowB["Gender"],
        "Age": rowB["Age"],
        "Ther": rowB["Ther"],
        "Outcome": rowB["Outcome"],
        "Vac": rowB["Vac"],
        "isMono": rowB["isMono"],
        "Result_D": rowB["Результат_D"],
        "Result_F": rowB["Результат_F"]
    }, ignore_index=True)

resGroupA.to_excel('.\\groups\\group_A.xlsx', index=False)
resGroupB.to_excel('.\\groups\\group_B.xlsx', index=False)
resGroupC.to_excel('.\\groups\\group_A_undefined_data.xlsx', index=False)
resGroupD.to_excel('.\\groups\\group_B_undefined_data.xlsx', index=False)

# res = pd.DataFrame(columns=["CaseID_A", "CaseID_B", "Age_A", "Age_B", "Gender", "Result_D_A", "Result_D_B", "Result_F_A", "Result_F_B", "Vac_A", "Vac_B"])
#
# for indexA, rowA in groupA.iterrows():
#     if indexA % 100 == 0: print(indexA)
#     for indexB, rowB in groupB.iterrows():
#         if (rowA["Gender"] == rowB["Gender"] and
#                 rowA["Vac"] == rowB["Vac"] and
#                 abs(rowA["Age"] - rowB["Age"]) <= 3 and
#                 resDgroupA[indexA] and resDgroupB[indexB] and
#                 abs(rowA["Результат_D"] - rowB["Результат_D"]) / rowA["Результат_D"] <= 0.1 and
#                 resFgroupA[indexA] and resFgroupB[indexB] and
#                 abs(rowA["Результат_F"] - rowB["Результат_F"]) / rowA["Результат_F"] <= 0.1):
#             res = res._append({"CaseID_A": rowA["CaseID"], "CaseID_B": rowB["CaseID"],
#                                "Age_A": rowA["Age"], "Age_B": rowB["Age"], "Gender": rowA["Gender"],
#                                "Result_D_A": rowA["Результат_D"], "Result_D_B": rowB["Результат_D"],
#                                "Result_F_A": rowA["Результат_F"], "Result_F_B": rowB["Результат_F"],
#                                "Vac_A": rowA["Vac"], "Vac_B": rowB["Vac"]}, ignore_index=True)
#
# res.to_excel('.\\data\\results_task3_with_similar_vac.xlsx', index=False)
