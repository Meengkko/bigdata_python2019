import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


plt.rcParams['figure.figsize'] = [12, 8]
data_set = pd.read_excel('test_ver1.01.xlsx', encoding='cp949', index_col=0)

# print(data_set.head(10))
# print(data_set.count())

fig, ax = plt.subplots(figsize=(20, 20))
sns.heatmap(data_set.corr(), ax=ax, cmap='coolwarm')
plt.show()


plt.plot('detached',  # x
         'college_grad',  # y
         data=data_set,
         linestyle='none',
         marker='o',
         markersize=10,
         color='blue',
         alpha=0.5)

plt.title('Scatter Plot of dataset by matplotlib', fontsize=20)
plt.xlabel('detached', fontsize=14)
plt.ylabel('college_grad', fontsize=14)
plt.show()


sns.regplot(x=data_set['detached'], y=data_set['college_grad'], fit_reg=True)
plt.title("Scatter plot with regression line by regplot()", fontsize=20)
plt.show()


sns.pairplot(data_set, diag_kind='hist')
plt.show()


data_set_shorten = data_set.iloc[:, :16]
sns.pairplot(data_set_shorten, diag_kind='kde', palette='bright')
plt.show()


print(list(data_set.columns))


