import pandas as pd

# dataframe = pd.read_excel('.\\data\\финальные_данные.xlsx')
# groupA = pd.read_excel('.\\groups\\isMono_false.xlsx')
# groupB = pd.read_excel('.\\groups\\isMono_true.xlsx')
#
# pattern1 = r'.*крайне тяжелое течение.*'
# pattern2 = r'.*среднетяжелое течение.*'
# pattern3 = r'.*тяжелое течение.*'
#
# maskA_1 = groupA["Ther"].str.contains(r'.*крайне тяжелое течение.*', na=False, regex=True)
# maskA_2 = groupA["Ther"].str.contains(r'.*тяжелое течение.*', na=False, regex=True)
# maskA_3 = groupA["Ther"].str.contains(r'.*среднетяжелое течение.*', na=False, regex=True)
# groupA.loc[maskA_1, "Ther"] = 1
# groupA.loc[maskA_2, "Ther"] = 2
# groupA.loc[maskA_3, "Ther"] = 3
#
# maskB_1 = groupB["Ther"].str.contains(r'.*крайне тяжелое течение.*', na=False, regex=True)
# maskB_2 = groupB["Ther"].str.contains(r'.*тяжелое течение.*', na=False, regex=True)
# maskB_3 = groupB["Ther"].str.contains(r'.*среднетяжелое течение.*', na=False, regex=True)
# groupB.loc[maskB_1, "Ther"] = 1
# groupB.loc[maskB_2, "Ther"] = 2
# groupB.loc[maskB_3, "Ther"] = 3
#
# res = pd.DataFrame(columns=["CaseID_A", "CaseID_B", "Age_A", "Age_B", "Gender", "Ther_A", "Ther_B", "Outcome_A", "Outcome_B", "Result_D_A", "Result_D_B", "Result_F_A", "Result_F_B", "Vac_A", "Vac_B"])
#
# ther = {
#     1: "крайне тяжелое течение",
#     2: "тяжелое течение",
#     3: "среднетяжелое течение"
# }
#
# for indexA, rowA in groupA.iterrows():
#     if indexA % 100 == 0: print(indexA)
#     for indexB, rowB in groupB.iterrows():
#         if (rowA["Gender"] == rowB["Gender"] and
#                 abs(rowA["Age"] - rowB["Age"]) <= 3 and
#                 abs(rowA["Результат_D"] - rowB["Результат_D"]) / rowA["Результат_D"] <= 0.1 and
#                 abs(rowA["Результат_F"] - rowB["Результат_F"]) / rowA["Результат_F"] <= 0.1 and
#                 ((rowA["Ther"] == 1 or rowA["Ther"] == 2) and (rowB["Ther"] == 1 or rowB["Ther"] == 2) or
#                  rowA["Ther"] == 3 and rowB["Ther"] == 3)):
#             res = res._append({"CaseID_A": rowA["CaseID"],
#                                "CaseID_B": rowB["CaseID"],
#                                "Age_A": rowA["Age"],
#                                "Age_B": rowB["Age"],
#                                "Gender": rowA["Gender"],
#                                "Ther_A": ther[rowA["Ther"]],
#                                "Ther_B": ther[rowB["Ther"]],
#                                "Outcome_A": rowA["Outcome"],
#                                "Outcome_B": rowB["Outcome"],
#                                "Result_D_A": rowA["Результат_D"],
#                                "Result_D_B": rowB["Результат_D"],
#                                "Result_F_A": rowA["Результат_F"],
#                                "Result_F_B": rowB["Результат_F"],
#                                "Vac_A": rowA["Vac"],
#                                "Vac_B": rowB["Vac"]}, ignore_index=True)
#
# res.to_excel('.\\data\\results_task3.xlsx', index=False)
#table for 3
#1 кол-во
data = pd.read_excel('data\\results_task3.xlsx')
dataTher = data['Ther_A'].value_counts();
dataHard = dataTher.get('тяжелое течение')
dataEasy = dataTher.get('среднетяжелое течение')
#2 выж - мость
dataAliveHardA = data[(data['Outcome_A'] == 'Выписан') & (data['Ther_A'] == 'тяжелое течение')]
dataAliveHardB = data[(data['Outcome_B'] == 'Выписан') & (data['Ther_B'] == 'тяжелое течение')]
dataDeathHardA = data[(data['Outcome_B'] == 'Умер') & (data['Ther_B'] == 'тяжелое течение')]
dataDeathHardB = data[(data['Outcome_B'] == 'Умер') & (data['Ther_B'] == 'тяжелое течение')]
countliveA = len(dataAliveHardA)/2
countDeathА = len(dataDeathHardA)/2
countliveB = len(dataAliveHardB)/2
countDeathB = len(dataDeathHardB)/2
pAleveHard = (countliveA + countliveB)/(countliveA + countliveB + countDeathА + countDeathB)

dataAliveHardA = data[(data['Outcome_A'] == 'Выписан') & (data['Ther_A'] == 'среднетяжелое течение')]
dataAliveHardB = data[(data['Outcome_B'] == 'Выписан') & (data['Ther_B'] == 'среднетяжелое течение')]
dataDeathHardA = data[(data['Outcome_B'] == 'Умер') & (data['Ther_B'] == 'среднетяжелое течение')]
dataDeathHardB = data[(data['Outcome_B'] == 'Умер') & (data['Ther_B'] == 'среднетяжелое течение')]
countliveA = len(dataAliveHardA)/2
countDeathА = len(dataDeathHardA)/2
countliveB = len(dataAliveHardB)/2
countDeathB = len(dataDeathHardB)/2
pAleveEasy = (countliveA + countliveB)/(countliveA + countliveB + countDeathА + countDeathB)
#3 вакцинир -ны
dataHardVac = data[(data['Vac_A'] == 'Нет') & (data['Ther_A'] == 'тяжелое течение') ].value_counts();
dataEasyVac = data[(data['Vac_A'] == 'Нет') & (data['Ther_A'] == 'среднетяжелое течение')].value_counts();
allDataCount = len(data)
countHardV = len(dataHardVac)
countEasyV = len(dataEasyVac)
#4
allDataCountVac = len(data[data['Vac_A'] != 'Нет'])
dataAliveHardA = data[(data['Outcome_A'] == 'Выписан') & (data['Ther_A'] == 'тяжелое течение') & (data['Vac_A'] != 'Нет')]
dataAliveEasyA = data[(data['Outcome_A'] == 'Выписан') & (data['Ther_A'] == 'среднетяжелое течение') & (data['Vac_A'] != 'Нет')]
dataAliveHardB = data[(data['Outcome_B'] == 'Выписан') & (data['Ther_B'] == 'тяжелое течение') & (data['Vac_B'] != 'Нет')]
dataAliveEasyB = data[(data['Outcome_B'] == 'Выписан') & (data['Ther_B'] == 'среднетяжелое течение') & (data['Vac_B'] != 'Нет')]

# Подсчет количества строк в датафреймах dataAliveHardA и dataAliveHardB
countliveHard = (len(dataAliveHardA) + len(dataAliveHardB)) / 2

# Подсчет количества строк в датафреймах dataAliveEasyA и dataAliveEasyB
countliveEasy = (len(dataAliveEasyA) + len(dataAliveEasyB)) / 2

table = {
    'Среднетяжелое течение': [
        round((dataEasy / (dataHard + dataEasy)) * 100),  # Процент среднетяжелых случаев
        round(pAleveEasy * 100),  # Процент выписанных при среднетяжелом течении
        round((countEasyV / allDataCount) * 100),  # Процент выписанных среднетяжелых от общего числа
        round((countliveEasy / allDataCountVac) * 100)  # Процент выписанных среднетяжелых от Vac_A != 'Нет'
    ],
    'Тяжелое течение': [
        round((dataHard / (dataHard + dataEasy)) * 100),  # Процент тяжелых случаев
        round(pAleveHard * 100),  # Процент выписанных при тяжелом течении
        round((countHardV / allDataCount) * 100),  # Процент выписанных тяжелых от общего числа
        round((countliveHard / allDataCountVac) * 100)  # Процент выписанных тяжелых от Vac_A != 'Нет'
    ]
}
df = pd.DataFrame(table)
df.index = ['колличество %','выживаемость %','вакцинированы %', 'выживаемость вакцинированных %']
print(df)
df.to_excel('data\\statisticFor3Task.xlsx')