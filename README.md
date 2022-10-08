# LabLab.ai


## AI Algorithms , Application & Hardware for LabLab.ai competition



## Introduction:

*I built an AI model using machine learning to analysis the data we gathered from **NASA** using **“SKlearn”** which is a library in Python then by using **ML algorithms** and Made an application to simulate an algorithm predicts depending on the input whether a fire occurs or not 
*  



## Technologies:


* Python (3.9)
* Sklearn library
* Numpy library
* Pandas library
* Matplotlib library
* Seaborn library
* joblib library
*  SYS library
* MATLAB (2020)
  1. GUI
  1. Statistics & Machine Learning Toolbox
*  PyQt5
   1. QtWidgets
   1. QtCore
   1. QtGui

## Summary:

> I used ML to solve the problem in particular his library sklearn which is
located inside python and through dataset which contained scripts we used
NLP and in particular label encoder To convert the string into an integer so
that the algorithm can deal with the dataset then we divided the data into a
part train and a partial test. and then we entered the data divided by five
classification algorithms and we compared scores on their own through
model check and in particular cross-validation-score to find out which
algorithm is the best to deal with this data, then we entered the best
algorithm on metrics model where we used ROC AUC Score, classification
report, confusion matrix, zero one loss. then we saved model, and its weights
,and i have built an application using pyqt5  which works to receive the factors that may cause a fire from the datasets and sensors. Then when the button is pressed, the user will be told whether a fire is expected or not and also has the capability of visualizing this prediction.
>
### The Best Classification Algorithms:

1. DecisionTreeClassifier
1. RandomForestClassifier
1. GaussianNB


## Blocks of code

```
#NLP(convert string to int )
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
le.fit(NASA_Data['month'])
NASA_Data['month']=le.transform(NASA_Data['month'])
print(list(le.classes_))
le.fit(NASA_Data['day'])
NASA_Data['day']=le.transform(NASA_Data['day'])
NASA_Data.to_excel('nasa.xls',sheet_name='Sheet1')
```
```
from sklearn.naive_bayes import GaussianNB
#Applying GaussianNB Model 
GaussianNBModel = GaussianNB()
GaussianNBModel.fit(X_train, y_train)

#Calculating Details
print('GaussianNBModel Train Score is : ' , GaussianNBModel.score(X_train, y_train))
print('GaussianNBModel Test Score is : ' , GaussianNBModel.score(X_test, y_test))
#print('----------------------------------------------------')

#Calculating Prediction
y_pred = GaussianNBModel.predict(X_test)
y_pred_prob = GaussianNBModel.predict_proba(X_test)

```
```
#GUI Form
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
a = QApplication(sys.argv)
tree = QWidget()
tree.setGeometry(350, 80, 500, 400)
tree.setWindowTitle('Chase the fire')
tree.setWindowIcon(QIcon('232744b113523592.jpg'))
tree.setAutoFillBackground(True)
q = tree.palette()
q.setColor(tree.backgroundRole(), Qt.lightGray)
tree.setPalette(q)

```

## Classification Algorithms Accuracy:

| Algorithm  | train & test score |
| ------------- |:-------------:|
| DecisionTreeClassifier     | 1.0 & 1.0     |
| RandomForestClassifier     | 1.0 &1.0     |
| GaussianNB      | 0.9942196531791907  & 0.9941520467836257     |

```
#DecisionTreeClassifier

fpr Value  :  [0. 0. 1.]
tpr Value  :  [0. 1. 1.]
thresholds Value  :  [2 1 0]
ROCAUC Score :  1.0
Classification Report is :                precision    recall  f1-score   support

           0       1.00      1.00      1.00        85
           1       1.00      1.00      1.00        86

    accuracy                           1.00       171
   macro avg       1.00      1.00      1.00       171
weighted avg       1.00      1.00      1.00       171

Confusion Matrix is : 
 [[85  0]
 [ 0 86]]
Zero One Loss Value :  0
```
```
#RandomForestClassifier

fpr Value  :  [0. 0. 1.]
tpr Value  :  [0. 1. 1.]
thresholds Value  :  [2 1 0]
ROCAUC Score :  1.0
Classification Report is :                precision    recall  f1-score   support

           0       1.00      1.00      1.00        85
           1       1.00      1.00      1.00        86

    accuracy                           1.00       171
   macro avg       1.00      1.00      1.00       171
weighted avg       1.00      1.00      1.00       171

Confusion Matrix is : 
 [[85  0]
 [ 0 86]]
Zero One Loss Value :  0
```

```
#GaussianNB

fpr Value  :  [0.         0.01176471 1.        ]
tpr Value  :  [0. 1. 1.]
thresholds Value  :  [2 1 0]
ROCAUC Score :  0.9941176470588236
Classification Report is :                precision    recall  f1-score   support

           0       1.00      0.99      0.99        85
           1       0.99      1.00      0.99        86

    accuracy                           0.99       171
   macro avg       0.99      0.99      0.99       171
weighted avg       0.99      0.99      0.99       171

Confusion Matrix is : 
 [[84  1]
 [ 0 86]]
Zero One Loss Value :  1

```


## Embedded System 

to make sure that the hardware system you have to connect the I/O pins as shwone in the Embedded_System_Code file 
then you have to install the multibals liberaris to ensure that the system work smothly

### liberaris needs to installed:

* mpu6050-master
* SoftwareSerial.h
* DHT sensor library

**Note** don't forget to add a phone number that is attached in the sever.




🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/dina-mohammed-b695aa216/)
