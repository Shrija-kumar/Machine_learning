
#importing numpy for linear alogorithm
import numpy as np


# In[2]:

#importing pandas
import pandas as pd

#data visualization packages
import seaborn as sns

#importing algorithms
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

#importing the data
test_df = pd.read_csv("test.csv")
train_df = pd.read_csv("train.csv")

#analysing the data
print(train_df.head(10))

#number of missing values
print(train_df.isnull().sum())


# In[3]:

#remove cabin
train_df = train_df.drop(['Cabin'], axis = 1)
test_df = test_df.drop(['Cabin'], axis = 1)

#filling embark with the most common
print(train_df['Embarked'].describe())
data = [train_df,test_df]
for dataset in data:
    dataset['Embarked'] = dataset['Embarked'].fillna("S")
train_df = train_df.drop(['Embarked'], axis = 1)
test_df = test_df.drop(['Embarked'], axis = 1)

#converting float into int64
train_df['Fare'] = train_df['Fare'].astype(int)
print(train_df['Fare'].describe())

#drop name
train_df = train_df.drop(['Name'], axis = 1)
test_df = test_df.drop(['Name'], axis = 1)

#drop ticket
train_df = train_df.drop(['Ticket'], axis = 1)
test_df = test_df.drop(['Ticket'], axis = 1)

#drop age
train_df = train_df.drop(['Age'], axis = 1)
test_df = test_df.drop(['Age'], axis = 1)

#drop name
train_df = train_df.drop(['Fare'], axis = 1)
test_df = test_df.drop(['Fare'], axis = 1)


print(train_df.dtypes)

train_df['Survived'] = train_df['Survived'].astype(int)

print(train_df.head(10))

genders = {"male": 0, "female":1}
data = [train_df, test_df]
for dataset in data:
    dataset['Sex'] = dataset['Sex'].fillna(0)
    dataset['Sex'] = dataset['Sex'].map(genders)
print(train_df.head(10))   


# In[4]:


#building models
X_train = train_df.drop(['Survived'], axis = 1)
Y_train = train_df['Survived']
X_test  = test_df

#randomforest
random_forest = RandomForestClassifier(n_estimators = 100)
random_forest.fit(X_train, Y_train)
Y_prediction = random_forest.predict(X_test)
random_forest.score(X_train,Y_train)
acc_random_forest = round(random_forest.score(X_train, Y_train)*100,2)
print(acc_random_forest)




# In[6]:

print(Y_prediction)


# In[8]:

prediction =pd.DataFrame(Y_prediction)
print(prediction)


# In[14]:

open('test.csv', 'w')


# In[15]:

np.savetxt('test.csv',Y_prediction,delimiter=',')


# In[20]:

print(Y_prediction)


# In[ ]:



