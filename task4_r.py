import pandas as pd

dataframe = pd.read_excel('.\\data\\финальные_данные.xlsx')

boolArr = dataframe["Ther"].str.contains("среднетяжелое течение")
groupA = dataframe[boolArr]
groupB = dataframe[~boolArr]

# Функция для проверки возможности преобразования в float
def can_convert_to_float(value):
    try:
        if isinstance(value, str):
            value = value.replace('>', '').replace('<', '').strip()
        float(value)
        return True
    except ValueError:
        return False

# Фильтрация строк
groupA_filtered = groupA[groupA["Результат_D"].apply(can_convert_to_float)]
groupB_filtered = groupB[groupB["Результат_D"].apply(can_convert_to_float)]

# Преобразование столбца "Результат_D" в float
groupA_filtered["Результат_D"] = groupA_filtered["Результат_D"].apply(lambda x: float(x.replace('>', '').replace('<', '').strip()))
groupB_filtered["Результат_D"] = groupB_filtered["Результат_D"].apply(lambda x: float(x.replace('>', '').replace('<', '').strip()))