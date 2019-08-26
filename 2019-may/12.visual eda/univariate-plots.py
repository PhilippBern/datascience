import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import pandas as pd
import os
print(sns.__version__)
print(matplotlib.__version__)

path = 'E://'
titanic_train = pd.read_csv(os.path.join(path, 'train.csv'))
print(titanic_train.shape)
print(titanic_train.info())

#categorical columns: numerical EDA
pd.crosstab(index=titanic_train["Survived"], columns="count")
pd.crosstab(index=titanic_train["Pclass"], columns="count")  
pd.crosstab(index=titanic_train["Sex"],  columns="count")

#categorical columns: visual EDA
sns.countplot(x='Survived',data=titanic_train)
sns.countplot(x='Pclass',data=titanic_train)
sns.countplot(x='Sex',data=titanic_train)
sns.countplot(x='Fare', data=titanic_train)

#continuous features: visual EDA
titanic_train['Fare'].describe()
sns.boxplot(x='Fare',data=titanic_train)
sns.distplot(titanic_train['Fare'], hist=False)
sns.distplot(titanic_train['Fare'], kde=False)
sns.distplot(titanic_train['Fare'], bins=20, rug=True, kde=False)
sns.distplot(titanic_train['Fare'], bins=100, kde=False)

#continuous features: numerical EDA
titanic_train['Fare'].describe()
titanic_train.describe()
