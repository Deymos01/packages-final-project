import pandas as pd

dataframe = pd.read_excel('.\\data\\финальные_данные.xlsx')
groupA = pd.read_excel('.\\groups\\isMono_false.xlsx')
groupB = pd.read_excel('.\\groups\\isMono_true.xlsx')

res = pd.DataFrame(columns=["CaseID_A", "CaseID_B", "Age_A", "Age_B", "Gender", "Ther", "Outcome_A", "Outcome_B", "Result_D_A", "Result_D_B", "Result_F_A", "Result_F_B", "Vac_A", "Vac_B"])

for indexA, rowA in groupA.iterrows():
    if indexA % 100 == 0: print(indexA)
    for indexB, rowB in groupB.iterrows():
        if (rowA["Gender"] == rowB["Gender"] and
                abs(rowA["Age"] - rowB["Age"]) <= 3 and
                abs(rowA["Результат_D"] - rowB["Результат_D"]) / rowA["Результат_D"] <= 0.1 and
                abs(rowA["Результат_F"] - rowB["Результат_F"]) / rowA["Результат_F"] <= 0.1 and
                rowA["Ther"] == rowB["Ther"]):
            res = res._append({"CaseID_A": rowA["CaseID"],
                               "CaseID_B": rowB["CaseID"],
                               "Age_A": rowA["Age"],
                               "Age_B": rowB["Age"],
                               "Gender": rowA["Gender"],
                               "Ther": rowA["Ther"],
                               "Outcome_A": rowA["Outcome"],
                               "Outcome_B": rowB["Outcome"],
                               "Result_D_A": rowA["Результат_D"],
                               "Result_D_B": rowB["Результат_D"],
                               "Result_F_A": rowA["Результат_F"],
                               "Result_F_B": rowB["Результат_F"],
                               "Vac_A": rowA["Vac"],
                               "Vac_B": rowB["Vac"]}, ignore_index=True)

res.to_excel('.\\data\\results_task3.xlsx', index=False)
