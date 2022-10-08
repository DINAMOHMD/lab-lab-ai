# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 18:38:18 2022

@author: pc
"""

#Call Dataset

import pandas as pd
convert_Data=pd.read_excel('nasa.xls')
X=convert_Data.iloc[:,:-1].values
y=convert_Data.iloc[:,-1].values


#----------------------------------------------------
#Splitting data

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=44, shuffle =True)

#----------------------------------------------------
from sklearn.tree import DecisionTreeClassifier

#Applying DecisionTreeClassifier Model 

DecisionTreeClassifierModel = DecisionTreeClassifier(criterion='gini',max_depth=2,random_state=33) 
DecisionTreeClassifierModel.fit(X_train, y_train)

#Calculating Details
print('DecisionTreeClassifierModel Train Score is : ' , DecisionTreeClassifierModel.score(X_train, y_train))
print('DecisionTreeClassifierModel Test Score is : ' , DecisionTreeClassifierModel.score(X_test, y_test))
#print('DecisionTreeClassifierModel Classes are : ' , DecisionTreeClassifierModel.classes_)
#print('DecisionTreeClassifierModel feature importances are : ' , DecisionTreeClassifierModel.feature_importances_)
#print('----------------------------------------------------')

#Calculating Prediction
y_pred = DecisionTreeClassifierModel.predict(X_test)
#y_pred_prob = DecisionTreeClassifierModel.predict_proba(X_test)
#print('Predicted Value for DecisionTreeClassifierModel is : ' , y_pred[:10])
#print('Prediction Probabilities Value for DecisionTreeClassifierModel is : ' , y_pred_prob[:10])
#----------------------------------------------------
#classification metrics

from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
#Calculating Receiver Operating Characteristic :  
fprValue, tprValue, thresholdsValue = roc_curve(y_test,y_pred)
print('fpr Value  : ', fprValue)
print('tpr Value  : ', tprValue)
print('thresholds Value  : ', thresholdsValue)
plt.plot(fprValue, tprValue)
plt.xlim([0,1])
plt.ylim([0,1])
plt.title('ROC curve for forest fire classifier')
plt.xlabel('False Positive Rate(1-Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')

from sklearn.metrics import roc_auc_score
#Calculating ROC AUC Score:  
ROCAUCScore = roc_auc_score(y_test,y_pred, average='micro') #it can be : macro,weighted,samples
print('ROCAUC Score : ', ROCAUCScore)
#----------------------------------------------------
from sklearn.metrics import classification_report
#Calculating classification Report :  
ClassificationReport = classification_report(y_test,y_pred)
print('Classification Report is : ', ClassificationReport )
#----------------------------------------------------

from sklearn.metrics import confusion_matrix
import seaborn as sns
#Calculating Confusion Matrix
CM = confusion_matrix(y_test, y_pred)
print('Confusion Matrix is : \n', CM)

# drawing confusion matrix
sns.heatmap(CM, center = True)
plt.title('ROC curve for forest fire classifier')
plt.show()
#----------------------------------------------------

from sklearn.metrics import zero_one_loss
#Calculating Zero One Loss:  
ZeroOneLossValue = zero_one_loss(y_test,y_pred,normalize=False) 
print('Zero One Loss Value : ', ZeroOneLossValue )
#----------------------------------------------------
import joblib as jb
#model save
jb.dump(DecisionTreeClassifierModel,'save file.sav')
savedmodel=jb.load('save file.sav')
