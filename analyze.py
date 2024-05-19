import pandas as pd

bDWithoutMono = pd.read_excel('.\\data\\БД_без_моно_full.xlsx')
bDMono = pd.read_excel('.\\data\\БД_с_моно_full.xlsx')

# add column about mono
bDWithoutMono['isMono'] = False
bDMono['isMono'] = True
# rename
bDMono.rename(columns={"Vacin": "Vac"}, inplace=True)
# Concatenate the DataFrames by rows
concatenated_data = pd.concat([bDWithoutMono, bDMono])
# Найдем строки с отсутствующими значениями в столбце 'CaseID'
missing_caseid_mask = concatenated_data['CaseID'].isna()
# Присвоим уникальные идентификаторы для отсутствующих значений
concatenated_data.loc[missing_caseid_mask, 'CaseID'] = range(390078, missing_caseid_mask.sum() + 390078)
# Сортировка по 'CaseID' и 'Date' так, чтобы самые свежие даты были первыми
concatenated_data = concatenated_data.sort_values(by='Start')
# Удаление дубликатов, оставляя только запись с самой свежей датой для каждого 'CaseID'
unique_data = concatenated_data.drop_duplicates(subset='CaseID', keep='first')
# save
unique_data.to_excel('.\\data\\Объединенные_данные.xlsx', index=False)
mergedData = pd.read_excel('.\\data\\Объединенные_данные.xlsx')
d1 = pd.read_excel('.\\data\\Показатель_D 1.xlsx')
f1 = pd.read_excel('.\\data\\Показатель_F 1.xlsx')
d_stat = d1.drop_duplicates(subset="CaseID")

f_stat = (f1.sort_values(["Дата взятия"])).drop_duplicates(subset="CaseID")

f_stat.rename(columns={"Результат": "Результат_F"}, inplace=True)
union_results_df = pd.merge(d_stat[["CaseID", "Результат_D"]], f_stat[["CaseID", "Результат_F"]], on="CaseID", how="inner")
union_result = pd.merge(mergedData, union_results_df, on="CaseID", how="inner")
union_result.to_excel('.\\data\\финальные_данные.xlsx', index=False)
(pd.concat([union_result.loc[union_result["Outcome"] == "Умер"], union_result.loc[union_result["Outcome"] == "Выписан"]])).to_excel(".\\data\\isalive.xlsx")

print("Done!")
