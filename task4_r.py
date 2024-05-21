import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency

dataframe_groupA = pd.read_excel('.\\groups\\group_A.xlsx')  # среднетяжелое течение болезни
dataframe_groupB = pd.read_excel('.\\groups\\group_B.xlsx')  # тяжелое течение болезни

# dataframe_groupA_incorrect_data = pd.read_excel('.\\groups\\group_A_undefined_data.xlsx')
# dataframe_groupB_incorrect_data = pd.read_excel('.\\groups\\group_B_undefined_data.xlsx')

ageA = dataframe_groupA["Age"]
ageB = dataframe_groupB["Age"]

t_stat_age, p_val_age = ttest_ind(ageA, ageB, equal_var=False)
print(f"Age: t-statistic = {t_stat_age}, p-value = {p_val_age}")

result_d_A = dataframe_groupA["Result_D"]
result_d_B = dataframe_groupB["Result_D"]

t_stat_result_d, p_val_result_d = ttest_ind(result_d_A, result_d_B, equal_var=False)
print(f"Result_D: t-statistic = {t_stat_result_d}, p-value = {p_val_result_d}")

result_f_A = dataframe_groupA["Result_F"]
result_f_B = dataframe_groupB["Result_F"]

t_stat_result_f, p_val_result_f = ttest_ind(result_f_A, result_f_B, equal_var=False)
print(f"Result_F: t-statistic = {t_stat_result_f}, p-value = {p_val_result_f}")

contingency_table_gender = pd.crosstab(dataframe_groupA["Gender"], dataframe_groupB["Gender"])
chi2_gender, p_value_gender, _, _ = chi2_contingency(contingency_table_gender)
print(f"Gender comparison p-value: {p_value_gender}")

