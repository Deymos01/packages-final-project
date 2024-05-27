print(5)
import pandas as pd
import matplotlib.pyplot as plt
#
# # Загрузка данных из Excel файла
data = pd.read_excel('.\\data\\финальные_данные.xlsx')

# Преобразование колонок 'Start' и 'End' в формат datetime и выделение часов
data['Start'] = pd.to_datetime(data['Start']).dt.day + 30 * pd.to_datetime(data['Start']).dt.month + 365 * pd.to_datetime(data['Start']).dt.year
data['End'] = pd.to_datetime(data['End']).dt.day + 30 * pd.to_datetime(data['End']).dt.month + 365 * pd.to_datetime(data['End']).dt.year
print(data)
data['Difference'] = data['End'] - data['Start']

# Сортировка разностей
sorted_differences = data['Difference'].sort_values()
# Извлечение значений из sorted_differences в pd.Series
sorted_differences_values = pd.Series(sorted_differences.values)


# Построение гистограммы с логарифмической шкалой по оси Y
plt.figure(figsize=(10, 6))
plt.hist(sorted_differences_values, bins=30, edgecolor='black')
plt.yscale('log')
plt.title('Length of stay of people in hospital')
plt.xlabel('days')
plt.ylabel('People count')
plt.grid(True, which="both", ls="--")
plt.show()

# Построение коробки с усами (box plot)
plt.figure(figsize=(10, 6))
plt.boxplot(sorted_differences_values, vert=False)
plt.title('Length of stay of people in hospital')
plt.xlabel('days')
plt.ylabel('People count')
plt.grid(True, which="both", ls="--")
plt.show()








