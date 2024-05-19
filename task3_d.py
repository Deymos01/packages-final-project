import pandas as pd
result_data = pd.read_excel('.\\data\\финальные_данные.xlsx')



bool_inf = result_data["Ther"].str.contains("среднетяжелое")
mid = result_data.loc[bool_inf]
hard = result_data.loc[~bool_inf]
# mid = result_data.loc[result_data["Ther"].str.contains("среднетяжелое")]

bool_type = mid['Результат_D'].apply(lambda x: isinstance(x, float) or isinstance(x, int))
print(bool_type)
print(mid.head())
# print(hard.info())
# print(mid.head())