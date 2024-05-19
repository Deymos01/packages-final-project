import numpy as np
import pandas as pd

# bDWithoutMono = pd.read_excel('data\БД_без_моно_full.xlsx')
# bDMono = pd.read_excel('data\БД_с_моно_full.xlsx')
#
# # add column about mono
# bDWithoutMono['isMono'] = False
# bDMono['isMono'] = True
# # rename
# bDMono.rename(columns={"Vacin": "Vac"}, inplace=True)
# # Concatenate the DataFrames by rows
# concatenated_data = pd.concat([bDWithoutMono, bDMono])
# # Найдем строки с отсутствующими значениями в столбце 'CaseID'
# missing_caseid_mask = concatenated_data['CaseID'].isna()
# # Присвоим уникальные идентификаторы для отсутствующих значений
# concatenated_data.loc[missing_caseid_mask, 'CaseID'] = range(390078, missing_caseid_mask.sum() + 390078)
# # Сортировка по 'CaseID' и 'Date' так, чтобы самые свежие даты были первыми
# concatenated_data = concatenated_data.sort_values(by='Start')
# # Удаление дубликатов, оставляя только запись с самой свежей датой для каждого 'CaseID'
# unique_data = concatenated_data.drop_duplicates(subset='CaseID', keep='first')
# # save
# unique_data.to_excel('data\Объединенные_данные.xlsx', index=False)
# mergedData = pd.read_excel('data\Объединенные_данные.xlsx')
# d1 = pd.read_excel('data\Показатель_D 1.xlsx')
# f1 = pd.read_excel('data\Показатель_F 1.xlsx')
# d_stat = d1.drop_duplicates(subset="CaseID")
#
# f_stat = (f1.sort_values(["Дата взятия"])).drop_duplicates(subset="CaseID")
#
# f_stat.rename(columns={"Результат": "Результат_F"}, inplace=True)
# union_results_df = pd.merge(d_stat[["CaseID", "Результат_D"]], f_stat[["CaseID", "Результат_F"]], on="CaseID", how="inner")
# union_result = pd.merge(mergedData, union_results_df, on="CaseID", how="inner")
# union_result.to_excel('data\финальные_данные.xlsx', index=False)
# (pd.concat([union_result.loc[union_result["Outcome"] == "Умер"], union_result.loc[union_result["Outcome"] == "Выписан"]])).to_excel("data\\isalive.xlsx")

# 2
# data = pd.read_excel('data\финальные_данные.xlsx')
# dataVac = data[(data['Vac'].notnull()) & (data['Vac'] != 'Нет')]
# dataVac.to_excel('data2\people_who_was_vaccinated.xlsx')
# dataWithoutVac = data.loc[data['Vac'] == 'Нет']
# dataWithoutVac.to_excel('data2\people_who_was`t_vaccinated.xlsx')
# noInfo = data[pd.isnull(data['Vac'])]
# noInfo.to_excel('data2\people_no_info.xlsx')
data = pd.read_excel('data\\финальные_данные.xlsx')
dataVac = pd.read_excel('data2\\people_who_was_vaccinated.xlsx')
noInfo =  pd.read_excel('data2\\people_no_info.xlsx')
dataWithoutVac =  pd.read_excel('data2\\people_who_was`t_vaccinated.xlsx')

allPeople = round(data.shape[0])
vaccinated = round(dataVac.shape[0] * 100/allPeople)
notVaccinated = round(dataWithoutVac.shape[0] * 100/allPeople)
noInformation = round(noInfo.shape[0] * 100/allPeople)
print(allPeople)
print(vaccinated)
print(notVaccinated)
print(noInformation)

data = {
    'vaccinated': ['%', 'муж', 'жен', 'выжило', 'не выжило', '% выживших'],
    'not vaccinated': ['%', 'муж', 'жен', 'выжило', 'не выжило', '% выживших'],
    'no info': ['%', 'муж', 'жен', 'выжило', 'не выжило', '% выживших']
}
df = pd.DataFrame(data)
df.index = ['%', 'муж', 'жен', 'выжило', 'не выжило', '% выживших']
#pull %
df.at['%', 'vaccinated'] = vaccinated
df.at['%', 'not vaccinated'] = notVaccinated
df.at['%', 'no info'] = noInformation
#pull муж
vaccinated = dataVac['Gender'].value_counts();
vaccinated = vaccinated.get('м')
notVaccinated = dataWithoutVac['Gender'].value_counts();
notVaccinated = notVaccinated.get('м')
noInformation = noInfo['Gender'].value_counts();
noInformation = noInformation.get('м')
df.at['муж', 'vaccinated'] = vaccinated
df.at['муж', 'not vaccinated'] = notVaccinated
df.at['муж', 'no info'] = noInformation
# pull жен
vaccinated = dataVac['Gender'].value_counts();
vaccinated = vaccinated.get('ж')
notVaccinated = dataWithoutVac['Gender'].value_counts();
notVaccinated = notVaccinated.get('ж')
noInformation = noInfo['Gender'].value_counts();
noInformation = noInformation.get('ж')
df.at['жен', 'vaccinated'] = vaccinated
df.at['жен', 'not vaccinated'] = notVaccinated
df.at['жен', 'no info'] = noInformation
# pull выжило
vaccinated = dataVac['Outcome'].value_counts();
vaccinated = vaccinated.get('Выписан')
notVaccinated = dataWithoutVac['Outcome'].value_counts();
notVaccinated = notVaccinated.get('Выписан')
noInformation = noInfo['Outcome'].value_counts();
noInformation = noInformation.get('Выписан')
df.at['выжило', 'vaccinated'] = vaccinated
df.at['выжило', 'not vaccinated'] = notVaccinated
df.at['выжило', 'no info'] = noInformation
# pull не выжило
vaccinated = dataVac['Outcome'].value_counts();
vaccinated = vaccinated.get('Умер')
notVaccinated = dataWithoutVac['Outcome'].value_counts();
notVaccinated = notVaccinated.get('Умер')
noInformation = noInfo['Outcome'].value_counts();
noInformation = noInformation.get('Умер')
df.at['не выжило', 'vaccinated'] = vaccinated
df.at['не выжило', 'not vaccinated'] = notVaccinated
df.at['не выжило', 'no info'] = noInformation
# pull % выжило
vaccinated = dataVac['Outcome'].value_counts();
sumVaccinated = vaccinated.get('Умер') + vaccinated.get('Выписан')
vaccinated = round(vaccinated.get('Выписан') *100 / sumVaccinated)
notVaccinated = dataWithoutVac['Outcome'].value_counts();
sumNotVaccinated = notVaccinated.get('Умер') + notVaccinated.get('Выписан')
notVaccinated = round(notVaccinated.get('Выписан') *100 / sumNotVaccinated)
noInformation = noInfo['Outcome'].value_counts();
sumNoInformation = noInformation.get('Умер') + noInformation.get('Выписан')
noInformation = round(noInformation.get('Выписан') *100 / sumNoInformation)
df.at['% выживших', 'vaccinated'] = vaccinated
df.at['% выживших', 'not vaccinated'] = notVaccinated
df.at['% выживших', 'no info'] = noInformation
df.to_excel('data2\\statistic.xlsx')