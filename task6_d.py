import pandas as pd
import matplotlib.pyplot as plt

isMono = pd.read_excel('data\\БД_с_моно_full.xlsx')
noMono = pd.read_excel('data\\БД_без_моно_full.xlsx')


# Вывод графика соотношения возрастов:
# age_counts = isMono['Age'].value_counts(normalize=True).sort_index()*100
isMono['Outcome'] = (isMono['Outcome'] == 'Выписан')
age_counts = isMono.groupby('Age')['Outcome'].mean()*100
plt.figure(figsize=(10, 6))
# plt.hist(isMono['Age'], bins=range(min(isMono['Age']), max(isMono['Age']) + 2), edgecolor='black', align='left')
plt.plot(age_counts.index, age_counts.values, marker='o', label='with mono')
plt.xlabel('Age')
plt.ylabel('Survival rate')
plt.title('Age distribution according to outcome')
plt.xticks(range(min(isMono['Age']), max(isMono['Age']) + 1, 10))
plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()

noMono['Outcome'] = (noMono['Outcome'] == 'Выписан')
# age_counts = noMono['Age'].value_counts(normalize=True).sort_index()*100
age_counts = noMono.groupby('Age')['Outcome'].mean()*100
plt.plot(age_counts.index, age_counts.values, marker='o', label='with no mono')
# plt.xlabel('Age')
# plt.ylabel('Percentage')
plt.xticks(range(min(noMono['Age']), max(noMono['Age']) + 1, 10))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.show()






# Сравнение по факту вакцинации
data_vac = pd.read_excel('data2\\people_who_was_vaccinated.xlsx')
data_novac = pd.read_excel('data2\\people_who_was`t_vaccinated.xlsx')
data_vac = data_vac[data_vac['Outcome'].isin(['Выписан', 'Умер'])]
data_vac['Outcome'] = data_vac['Outcome'] == 'Выписан'
data_novac = data_novac[data_novac['Outcome'].isin(['Выписан', 'Умер'])]
data_novac['Outcome'] = data_novac['Outcome'] == 'Выписан'

mono_factor = data_vac.groupby('isMono')['Outcome'].mean() * 100
plt.figure(figsize=(10, 6))
mono_factor.plot(kind='bar', color=['blue', 'green'])
plt.xlabel('is mono')
plt.ylabel('Survival Rate (%)')
plt.title('Impact mono for vaccinated')
plt.xticks(rotation=0)  # Поворот меток по оси x для удобства чтения
plt.yticks(range(0, 101, 10))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
mono_factor = data_novac.groupby('isMono')['Outcome'].mean() * 100
plt.figure(figsize=(10, 6))
mono_factor.plot(kind='bar', color=['blue', 'green'])
plt.xlabel('is mono')
plt.ylabel('Survival Rate (%)')
plt.title('Impact mono for not vaccinated')
plt.xticks(rotation=0)  # Поворот меток по оси x для удобства чтения
plt.yticks(range(0, 101, 10))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()






# График зависимости выживаемости от пола
unit_data = pd.read_excel('data\\Объединенные_данные.xlsx')
unit_data = unit_data[unit_data['Outcome'].isin(['Выписан', 'Умер'])]
unit_data['Outcome'] = (unit_data['Outcome'] == 'Выписан')
gender_factor = unit_data.groupby('Gender')['Outcome'].mean() * 100
plt.figure(figsize=(10, 6))
# gender_factor.plot(kind='bar', color=['blue', 'green'])
plt.bar(gender_factor.index, gender_factor.values, color=['blue', 'green'])
plt.xlabel('Gender')
plt.ylabel('Survival Rate (%)')
plt.title('Impact gender for survival rate')
plt.xticks(gender_factor.index, ['Female', 'Male'])
plt.yticks(range(0, 101, 10))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
print(gender_factor)







# Тяжесть заболевания
isalive = pd.read_excel('data\\isalive.xlsx')
isalive['Outcome'] = (isalive['Outcome'] == 'Выписан')
severity_factor = isalive.groupby('Ther')['Outcome'].mean() * 100
severity_factor = severity_factor.sort_index(ascending=False)
plt.figure(figsize=(10, 8))
sev = ['ИНФ (среднетяжелое течение) с терапией и ЛП',
'ИНФ (среднетяжелое течение) с терапией без ЛП',
'ИНФ (среднетяжелое течение) с ЛП без терапии',
'ИНФ (среднетяжелое течение) без ЛП и терапии',
'ИНФ (тяжелое течение) с терапией и ЛП',
'ИНФ (тяжелое течение) с терапией без ЛП',
'ИНФ (тяжелое течение) без ЛП и терапии',
'ИНФ (крайне тяжелое течение) с терапией без ЛП',
'ИНФ (крайне тяжелое течение) без ЛП и терапии',
'ИНФ (крайне  тяжелое течение) с терапией и ЛП']
print(sev)
vall = severity_factor.values
vall[3], vall[6] = vall[6], vall[3]
vall[5], vall[6] = vall[6], vall[5]
vall[5], vall[4] = vall[4], vall[5]
vall[0], vall[4] = vall[4], vall[0]
vall[1], vall[5] = vall[5], vall[1]
vall[2], vall[6] = vall[6], vall[2]

plt.bar(sev, severity_factor.values, color=['blue', 'blue', 'blue', 'blue', 'orange', 'orange', 'orange', 'red', 'red', 'red'])
# plt.bar['ИНФ (среднетяжелое течение) с терапией и ЛП']
plt.xlabel('Ther')
plt.ylabel('Survival Rate (%)')
plt.title('Impact severity for survival rate')
# plt.xticks(severity_factor.index, ['T&LP', 'T', 'LP', 'nothing', 'T&LP', 'T', 'nothing', 'T', 'nothing', 'T&LP'],rotation=0)
plt.xticks(sev, ['T&LP', 'T', 'LP', 'nothing', 'T&LP', 'T', 'nothing', 'T', 'nothing', 'T&LP'],rotation=0)
plt.yticks(range(0, 101, 10))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()







