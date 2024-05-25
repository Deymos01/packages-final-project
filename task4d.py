import pandas as pd
from scipy import stats

groupA = pd.read_excel('.\\groups\\isMono_false.xlsx')
groupB = pd.read_excel('.\\groups\\isMono_true.xlsx')

t_stat, p_stat = stats.ttest_ind(groupA['Age'], groupB['Age'], equal_var=True)
print('Age : t = ', t_stat, ' p = ', p_stat)
t_stat, p_stat = stats.ttest_ind(groupA['Результат_D'], groupB['Результат_D'], equal_var=True)
print('Result_D : t = ', t_stat, ' p = ', p_stat)
t_stat, p_stat = stats.ttest_ind(groupA['Результат_F'], groupB['Результат_F'], equal_var=True, nan_policy='omit')
print('Result_F : t = ', t_stat, ' p = ', p_stat)

print(groupA['Age'].describe())
print(groupB['Age'].describe())

