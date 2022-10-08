# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 18:44:02 2022

@author: pc
"""
#Call Dataset

import pandas as pd
NASA_Data=pd.read_csv('Full.csv')

#----------------------------------------------------
#NLP(convert string to int )

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
le.fit(NASA_Data['month'])
NASA_Data['month']=le.transform(NASA_Data['month'])
print(list(le.classes_))
le.fit(NASA_Data['day'])
NASA_Data['day']=le.transform(NASA_Data['day'])
NASA_Data.to_excel('nasa.xls',sheet_name='Sheet1')
convert_Data=pd.read_excel('nasa.xls')
X=convert_Data.iloc[:,:-1].values
y=convert_Data.iloc[:,-1].values


#----------------------------------------------------
#Splitting data

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=44, shuffle =True)

#Splitted Data
#print('X_train shape is ' , X_train.shape)
#print('X_test shape is ' , X_test.shape)
#print('y_train shape is ' , y_train.shape)
#print('y_test shape is ' , y_test.shape)

#----------------------------------------------------

#model check

from sklearn.linear_model import SGDClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB



model1 =  SGDClassifier(penalty='l2',loss='squared_loss',learning_rate='optimal',random_state=33)
model2 = SVC(kernel= 'rbf',# it can be also linear,poly,sigmoid,precomputed
               max_iter=100,C=1.0,gamma='auto')
model3 = DecisionTreeClassifier(criterion='gini',max_depth=3,random_state=33)
model4=RandomForestClassifier(criterion='gini',n_estimators=100,max_depth=3,random_state=33)
model5=GaussianNB()
models = [model1 , model2 , model3 , model4, model5]

x=0
for m in models:
    x+=1
    
    for n in range(2,5):
        print('result of model number : ' , x ,' for cv value ',n,' is ' , cross_val_score(m, X_train, y_train, cv=n))  
    print('=====================================')

x=0
for m in models:
     x+=1
     
     for n in range(2,5):
         print('result of model number : ' , x ,' for cv value ',n,' is ' , cross_val_score(m, X_test, y_test, cv=n))  
     print('***********************************')
      