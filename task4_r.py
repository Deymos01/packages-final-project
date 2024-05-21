import pandas as pd
from scipy.stats import ttest_ind

dataframe_groupA = pd.read_excel('.\\groups\\group_A.xlsx')  # среднетяжелое течение болезни
dataframe_groupB = pd.read_excel('.\\groups\\group_B.xlsx')  # тяжелое течение болезни

# dataframe_groupA_incorrect_data = pd.read_excel('.\\groups\\group_A_undefined_data.xlsx')
# dataframe_groupB_incorrect_data = pd.read_excel('.\\groups\\group_B_undefined_data.xlsx')

ageA = dataframe_groupA["Age"]
ageB = dataframe_groupB["Age"]

t_stat_age, p_val_age = ttest_ind(ageA, ageB, equal_var=False)
print(f"Age: t-statistic = {t_stat_age}, p-value = {p_val_age}")
