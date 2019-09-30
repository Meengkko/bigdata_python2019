# 목적: 변수별 서로 다른 통계량 구하기
import pandas as pd

# Read the data set into a pandas DataFrame
churn = pd.read_csv('churn.csv', sep=',', header=0)

churn.columns = [heading.lower() for heading in churn.columns.str.replace(' ', '_').str.replace("\'", "").str.strip('?')]


churn['total_charges'] = churn['day_charge'] + churn['eve_charge'] + churn['night_charge'] + churn['intl_charge']
factor_cut = pd.cut(churn.total_charges, 5, precision=2)

print("Debug] churn.pivot_table(['total_charge'], index=['churn', 'custserv_calls']))")
print(churn.pivot_table(['total_charges'], index=['churn', 'custserv_calls']))
print("\n\nDebug] churn.pivot_table(['total_charges'], index=['churn'], columns=['custserv_calls']))")
print(churn.pivot_table(['total_charges'], index=['churn'], columns=['custserv_calls']))
print("\nDebug]churn.pivot_table(['total_charges'], index=['custserv_calls'], columns=['churn'], aggfunc='mean', fill_value='NaN', margins=True))")
print(churn.pivot_table(['total_charges'], index=['custserv_calls'], columns=['churn'], aggfunc='mean', fill_value='NaN', margins=True))

