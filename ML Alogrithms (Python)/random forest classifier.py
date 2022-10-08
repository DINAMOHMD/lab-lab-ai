# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
# Import Libraries
from sklearn.ensemble import RandomForestClassifier

RandomForestClassifierModel = RandomForestClassifier(criterion = 'gini',n_estimators=100,max_depth=2,random_state=33)  
RandomForestClassifierModel.fit(X_train, y_train)
#----------------------------------------------------
#Calculating Details
print('RandomForestClassifierModel Train Score is : ' , RandomForestClassifierModel.score(X_train, y_train))
print('RandomForestClassifierModel Test Score is : ' , RandomForestClassifierModel.score(X_test, y_test))
#print('RandomForestClassifierModel features importances are : ' , RandomForestClassifierModel.feature_importances_)
#print('----------------------------------------------------')

#Calculating Prediction
y_pred = RandomForestClassifierModel.predict(X_test)
#y_pred_prob = RandomForestClassifierModel.predict_proba(X_test)
#print('Predicted Value for RandomForestClassifierModel is : ' , y_pred[:10])
#print('Prediction Probabilities Value for RandomForestClassifierModel is : ' , y_pred_prob[:10])
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
plt.show()
#----------------------------------------------------

from sklearn.metrics import zero_one_loss
#Calculating Zero One Loss:  
ZeroOneLossValue = zero_one_loss(y_test,y_pred,normalize=False) 
print('Zero One Loss Value : ', ZeroOneLossValue )
#----------------------------------------------------
import joblib as jb
#model save
jb.dump(RandomForestClassifierModel,'saved file.sav')
savedmodel=jb.load('saved file.sav')
