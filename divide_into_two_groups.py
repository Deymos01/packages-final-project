import pandas as pd

dataframe = pd.read_excel('.\\data\\финальные_данные.xlsx')
dataframe['Результат_D'] = pd.to_numeric(dataframe['Результат_D'], errors='coerce')
dataframe['Результат_F'] = pd.to_numeric(dataframe["Результат_F"], errors='coerce')
dataframe = dataframe.dropna(subset=["Vac"])
dataframe = dataframe.dropna(subset=["Результат_D"])
dataframe = dataframe.dropna(subset=["Результат_F"])

dataframeIsMono_true = dataframe[dataframe['isMono'] == True]
dataframeIsMono_false = dataframe[dataframe['isMono'] == False]

dataframeIsMono_true.to_excel(".\\groups\\isMono_true.xlsx", index=False)
dataframeIsMono_false.to_excel(".\\groups\\isMono_false.xlsx", index=False)
