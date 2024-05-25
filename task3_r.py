import pandas as pd

dataframe = pd.read_excel('.\\data\\финальные_данные.xlsx')
groupA = pd.read_excel('.\\groups\\isMono_false.xlsx')
groupB = pd.read_excel('.\\groups\\isMono_true.xlsx')

pattern1 = r'.*крайне тяжелое течение.*'
pattern2 = r'.*среднетяжелое течение.*'
pattern3 = r'.*тяжелое течение.*'

maskA_1 = groupA["Ther"].str.contains(r'.*крайне тяжелое течение.*', na=False, regex=True)
maskA_2 = groupA["Ther"].str.contains(r'.*тяжелое течение.*', na=False, regex=True)
maskA_3 = groupA["Ther"].str.contains(r'.*среднетяжелое течение.*', na=False, regex=True)
groupA.loc[maskA_1, "Ther"] = 1
groupA.loc[maskA_2, "Ther"] = 2
groupA.loc[maskA_3, "Ther"] = 3

maskB_1 = groupB["Ther"].str.contains(r'.*крайне тяжелое течение.*', na=False, regex=True)
maskB_2 = groupB["Ther"].str.contains(r'.*тяжелое течение.*', na=False, regex=True)
maskB_3 = groupB["Ther"].str.contains(r'.*среднетяжелое течение.*', na=False, regex=True)
groupB.loc[maskB_1, "Ther"] = 1
groupB.loc[maskB_2, "Ther"] = 2
groupB.loc[maskB_3, "Ther"] = 3

res = pd.DataFrame(columns=["CaseID_A", "CaseID_B", "Age_A", "Age_B", "Gender", "Ther_A", "Ther_B", "Outcome_A", "Outcome_B", "Result_D_A", "Result_D_B", "Result_F_A", "Result_F_B", "Vac_A", "Vac_B"])

ther = {
    1: "крайне тяжелое течение",
    2: "тяжелое течение",
    3: "среднетяжелое течение"
}

for indexA, rowA in groupA.iterrows():
    if indexA % 100 == 0: print(indexA)
    for indexB, rowB in groupB.iterrows():
        if (rowA["Gender"] == rowB["Gender"] and
                abs(rowA["Age"] - rowB["Age"]) <= 3 and
                abs(rowA["Результат_D"] - rowB["Результат_D"]) / rowA["Результат_D"] <= 0.1 and
                abs(rowA["Результат_F"] - rowB["Результат_F"]) / rowA["Результат_F"] <= 0.1 and
                ((rowA["Ther"] == 1 or rowA["Ther"] == 2) and (rowB["Ther"] == 1 or rowB["Ther"] == 2) or
                 rowA["Ther"] == 3 and rowB["Ther"] == 3)):
            res = res._append({"CaseID_A": rowA["CaseID"],
                               "CaseID_B": rowB["CaseID"],
                               "Age_A": rowA["Age"],
                               "Age_B": rowB["Age"],
                               "Gender": rowA["Gender"],
                               "Ther_A": ther[rowA["Ther"]],
                               "Ther_B": ther[rowB["Ther"]],
                               "Outcome_A": rowA["Outcome"],
                               "Outcome_B": rowB["Outcome"],
                               "Result_D_A": rowA["Результат_D"],
                               "Result_D_B": rowB["Результат_D"],
                               "Result_F_A": rowA["Результат_F"],
                               "Result_F_B": rowB["Результат_F"],
                               "Vac_A": rowA["Vac"],
                               "Vac_B": rowB["Vac"]}, ignore_index=True)

res.to_excel('.\\data\\results_task3.xlsx', index=False)
