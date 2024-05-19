import pandas as pd

mono = pd.read_excel('БД_с_моно_full.xlsx')
no_mono = pd.read_excel('БД_без_моно_full.xlsx')
d_stat = pd.read_excel('Показатель_D 1.xlsx')
f_stat = pd.read_excel('Показатель_F 1.xlsx')


# print(pd.merge(mono, no_mono, on='CaseID', how='inner'))
mono.rename(columns={"Vacin": "Vac"}, inplace=True)
mono['is_mono'] = True
no_mono['is_mono'] = False
union_mono = pd.concat([mono, no_mono]) # соединение по строкам


union_mono = pd.read_excel('Объединенные_данные.xlsx')
# print(sum((union_mono.duplicated(subset='CaseID'))))
union_mono = (union_mono.sort_values(["Start"])).drop_duplicates(subset="CaseID")
# print(sum((union_mono.duplicated(subset='CaseID'))))

# print(sum((d_stat.duplicated(subset='CaseID'))))
d_stat = d_stat.drop_duplicates(subset="CaseID")
# print(sum((d_stat.duplicated(subset='CaseID'))))

# print(sum((f_stat.duplicated(subset='CaseID'))))
f_stat = (f_stat.sort_values(["Дата взятия"])).drop_duplicates(subset="CaseID")
# print(sum((f_stat.duplicated(subset='CaseID'))))

f_stat.rename(columns={"Результат": "Результат_F"}, inplace=True)
union_results_df = pd.merge(d_stat[["CaseID", "Результат_D"]], f_stat[["CaseID", "Результат_F"]], on="CaseID", how="inner")


# print(mono.info())
# print(union_mono.columns)
# print(union_results_df.columns)

union_result = pd.merge(union_mono, union_results_df, on="CaseID", how="inner")
union_result.to_excel("result_table.xlsx")

# print(sum((union_result.duplicated(subset='CaseID'))))

# print(union_result.info())

# isalive = pd.DataFrame(union_result.columns)

(union_result.loc[union_result["Outcome"] == "Умер"]).to_excel("isalive.xlsx")

union_results_df.to_excel("DF con.xlsx")




# print(mono.info())
#
# print(no_mono.info())
# print(d_stat.info())
# print(f_stat.info())

