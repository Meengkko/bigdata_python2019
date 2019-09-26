# https://www.kaggle.com/marcovasquez/machine-learning-on-board-titanic-17-algothim

#foundational package for scientific computing
import numpy as np

#collection of functions for data processing and analysis modeled after R dataframes with SQL like features
import pandas as pd

#collection of functions for scientific and publication-ready visualization
import matplotlib.pyplot as plt

#Visualization
import seaborn as sns

#collection of functions for scientific computing and advance mathematics
import scipy as sp

#collection of machine learning algorithms
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier

#Common Model Helpers
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
from sklearn import model_selection
import pylab as pl


#ignore warnings
import warnings
warnings.filterwarnings('ignore')

datatrain = pd.read_csv('train.csv')
datatest = pd.read_csv('test.csv')

print(datatrain.shape)
print(datatest.shape)

print(datatrain.info())

print('Train columns with null values:\n{} \n' .format(datatrain.isnull().sum()))

print('Test columns with null values:\n{}'.format(datatest.isnull().sum()))

print(datatrain.describe())
print(datatest.describe())

#First datatrain

datatrain['Age'].fillna(datatrain['Age'].median(), inplace=True)
datatrain['Embarked'].fillna(datatrain['Embarked'].mode()[0], inplace=True)
datatrain['Fare'].fillna(datatrain['Fare'].median(), inplace=True)

#Now the datatest

datatest['Age'].fillna(datatest['Age'].median(), inplace=True)
datatest['Embarked'].fillna(datatest['Embarked'].mode()[0], inplace=True)
datatest['Fare'].fillna(datatest['Fare'].median(), inplace=True)

print('\nTrain columns with null values:\n{} \n' .format(datatrain.isnull().sum()))
print("*************************************")
print('Test columns with null values:\n{}'.format(datatest.isnull().sum()))

drop_column = ['PassengerId', 'Cabin', 'Ticket']
datatrain.drop(drop_column, axis=1, inplace=True)
datatest.drop(drop_column, axis=1, inplace=True)

alltables = [datatrain, datatest]

for dataset in alltables:
    # Discrete variables
    dataset['FamilySize'] = dataset['SibSp'] + dataset['Parch'] + 1

    dataset['IsAlone'] = 1  # initialize to yes/1 is alone
    dataset['IsAlone'].loc[dataset['FamilySize'] > 1] = 0  # now update to no/0 if family size is greater than 1

    # quick and dirty code split title from name: http://www.pythonforbeginners.com/dictionary/python-split
    dataset['Title'] = dataset['Name'].str.split(", ", expand=True)[1].str.split(".", expand=True)[0]

    # Continuous variable bins; qcut vs cut: https://stackoverflow.com/questions/30211923/what-is-the-difference-between-pandas-qcut-and-pandas-cut
    # Fare Bins/Buckets using qcut or frequency bins: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.qcut.html
    dataset['FareBin'] = pd.qcut(dataset['Fare'], 4)

    # Age Bins/Buckets using cut or value bins: https://pandas.pydata.org/pandas-docs/stable/generated/pandas.cut.html
    dataset['AgeBin'] = pd.cut(dataset['Age'].astype(int), 5)

# cleanup rare title names
# print(data1['Title'].value_counts())
stat_min = 10
# while small is arbitrary, we'll use the common minimum in statistics: http://nicholasjjackson.com/2012/03/08/sample-size-is-10-a-magic-number/

title_names = (datatrain[
                'Title'].value_counts() < stat_min)  # this will create a true false series with title name as index

# apply and lambda functions are quick and dirty code to find and replace with fewer lines of code: https://community.modeanalytics.com/python/tutorial/pandas-groupby-and-python-lambda-functions/
datatrain['Title'] = datatrain['Title'].apply(lambda x: 'Misc' if title_names.loc[x] == True else x)
print(datatrain['Title'].value_counts())
print("----------")

# preview data again
print(datatrain.info())
print(datatest.info())
print(datatrain.head())

sns.countplot(x="Survived", data=datatrain)  # How many people survived
plt.title("How many people survived")
# plt.show()


# fig, saxis = plt.subplots(2, 2,figsize=(16,12))
'''
sns.countplot(x='Survived', hue="Embarked", data=datatrain,ax = saxis[0,0])
sns.countplot(x='Survived', hue="IsAlone", data=datatrain,ax = saxis[0,1])
sns.countplot(x="Survived", hue="Pclass", data=datatrain, ax = saxis[1,0])
sns.countplot(x="Survived", hue="Sex", data=datatrain, ax = saxis[1,1])
'''
# plt.show()


# fig, (axis1,axis2,axis3) = plt.subplots(1,3,figsize=(14,12))
'''
sns.boxplot(x = 'Pclass', y = 'Fare', hue = 'Survived', data = datatrain, ax = axis1)
axis1.set_title('Pclass vs Fare Survival Comparison')

sns.violinplot(x = 'Pclass', y = 'Age', hue = 'Survived', data = datatrain, split = True, ax = axis2)
axis2.set_title('Pclass vs Age Survival Comparison')

sns.boxplot(x = 'Pclass', y ='FamilySize', hue = 'Survived', data = datatrain, ax = axis3)
axis3.set_title('Pclass vs Family Size Survival Comparison')
# plt.show()
'''
a = sns.FacetGrid( datatrain, hue = 'Survived', aspect=4 )
a.map(sns.kdeplot, 'Age', shade= True )
a.set(xlim=(0 , datatrain['Age'].max()))
a.add_legend()
plt.title('age distribution')

plt.subplots(figsize =(14, 12))
correlation = datatrain.corr()
sns.heatmap(correlation, annot=True,cmap='coolwarm')
# plt.show()

label = LabelEncoder()

for dataset in alltables:
    dataset['Sex_Code'] = label.fit_transform(dataset['Sex'])
    dataset['Embarked_Code'] = label.fit_transform(dataset['Embarked'])
    dataset['Title_Code'] = label.fit_transform(dataset['Title'])
    dataset['AgeBin_Code'] = label.fit_transform(dataset['AgeBin'])
    dataset['FareBin_Code'] = label.fit_transform(dataset['FareBin'])


#define y variable aka target/outcome
Target = ['Survived']

#define x variables for original features aka feature selection
datatrain_x = ['Sex','Pclass', 'Embarked', 'Title','SibSp', 'Parch', 'Age', 'Fare', 'FamilySize', 'IsAlone'] #pretty name/values for charts
datatrain_x_calc = ['Sex_Code','Pclass', 'Embarked_Code', 'Title_Code','SibSp', 'Parch', 'Age', 'Fare'] #coded for algorithm calculation
datatrain_xy =  Target + datatrain_x
print('Original X Y: ', datatrain_xy, '\n')


#define x variables for original w/bin features to remove continuous variables
datatrain_x_bin = ['Sex_Code','Pclass', 'Embarked_Code', 'Title_Code', 'FamilySize', 'AgeBin_Code', 'FareBin_Code']
datatrain_xy_bin = Target + datatrain_x_bin
print('Bin X Y: ', datatrain_xy_bin, '\n')


#define x and y variables for dummy features original
datatrain_dummy = pd.get_dummies(datatrain[datatrain_x])
datatrain_x_dummy = datatrain_dummy.columns.tolist()
datatrain_xy_dummy = Target + datatrain_x_dummy
print('Dummy X Y: ', datatrain_xy_dummy, '\n')

datatrain_dummy.head()

train1_x_dummy, test1_x_dummy, train1_y_dummy, test1_y_dummy = train_test_split(datatrain[datatrain_x_calc], datatrain[Target], random_state = 0)
train1_x_bin, test1_x_bin, train1_y_bin, test1_y_bin = model_selection.train_test_split(datatrain[datatrain_x_bin], datatrain[Target] , random_state = 0)

print("DataTrain Shape: {}".format(datatrain.shape))
print("Train1 Shape: {}".format(train1_x_dummy.shape))
print("Test1 Shape: {}".format(test1_x_dummy.shape))

# 1. Decision Tree
Model = DecisionTreeClassifier()

Model.fit(train1_x_dummy, train1_y_dummy)

y_predL = Model.predict(test1_x_dummy)

    # Summary of the predictions made by the classifier
print(classification_report(test1_y_dummy, y_predL))
print(confusion_matrix(test1_y_dummy, y_predL))
    # Accuracy score
print('accuracy is',accuracy_score(y_predL,test1_y_dummy))

DT = accuracy_score(y_predL,test1_y_dummy)


# 2. Random Forest
Model=RandomForestClassifier(max_depth=2)
Model.fit(train1_x_dummy, train1_y_dummy)
y_predR=Model.predict(test1_x_dummy)

# Summary of the predictions made by the classifier
print(classification_report(test1_y_dummy,y_predR))
print(confusion_matrix(y_predR,test1_y_dummy))
#Accuracy Score
print('accuracy is ',accuracy_score(y_predR,test1_y_dummy))

RT = accuracy_score(y_predR,test1_y_dummy)
