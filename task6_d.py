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






isMono['Vacin'] = (isMono['Vacin'] != 'Нет')
age_counts = isMono.groupby('Outcome')['Vacin'].mean()*100
plt.figure(figsize=(10, 6))
age_counts.plot(kind='bar', color=['blue', 'green'])
plt.xlabel('Drug Usage')
plt.ylabel('Survival Rate (%)')
plt.title('Survival Rate by Drug Usage')
plt.xticks(rotation=0)  # Поворот меток по оси x для удобства чтения
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
# plt.plot(age_counts.index, age_counts.values, marker='o', label='with mono')
# plt.xlabel('Outcome')
# plt.ylabel('Vacine rate')
# plt.title('Age distribution according to outcome')
# plt.xticks(range(min(isMono['Age']), max(isMono['Age']) + 1, 10))
# plt.grid(axis='y', linestyle='--', alpha=0.7)
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