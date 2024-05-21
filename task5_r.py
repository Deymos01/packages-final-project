import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

dataframe_groupA = pd.read_excel('.\\groups\\group_A.xlsx')  # среднетяжелое течение болезни
dataframe_groupB = pd.read_excel('.\\groups\\group_B.xlsx')  # тяжелое течение болезни

dataframe_groupA["Group"] = "Moderate"
dataframe_groupB["Group"] = "Severe"
dataframe = pd.concat([dataframe_groupA, dataframe_groupB], ignore_index=True)

# Сравнение количества пациентов в группах A и B (Dead|Alive)
plt.figure(figsize=(10, 6))
sns.countplot(data=dataframe, x="Group", hue="Outcome")
plt.title("Comparison of Outcomes (Alive/Deceased) Between Groups A and B")
plt.xlabel("Group")
plt.yscale("log")
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: int(x)))
plt.ylabel("Number of Patients")
plt.legend(title="Outcome")
plt.show()


dataframe['Start'] = pd.to_datetime(dataframe['Start'], format='%d/%m/%Y')
dataframe['End'] = pd.to_datetime(dataframe['End'], format='%d/%m/%Y')

# Рассчет длительности госпитализации
dataframe['Hospitalization_Days'] = (dataframe['End'] - dataframe['Start']).dt.days

# Визуализация
plt.figure(figsize=(10, 6))
sns.boxplot(data=dataframe, x='Group', y='Hospitalization_Days')
plt.title('Comparison of Hospitalization Days Between Groups A and B')
plt.xlabel('Group')
plt.ylabel('Hospitalization Days')
plt.show()