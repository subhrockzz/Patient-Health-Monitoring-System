import numpy as np
import pandas as pd
from time import sleep
# Importing the dataset
dataset = pd.read_csv('final.csv')
#Assigning the parameters And the Target Value
X=dataset.iloc[:, :-1].values
y = dataset.iloc[:, 7].values
#Deviding the Dataset into Train and Test
from sklearn import model_selection
X_train,X_test,y_train,y_test= model_selection.train_test_split(X, y, test_size = 0.2, random_state = 0) 
#Creating the ml_model
def create_model():
    from sklearn.linear_model import LinearRegression
    reg=LinearRegression()
    reg.fit(X_train,y_train)
    y_pred= reg.predict(X_test)
    return reg
ml_model=create_model()
#Realtime Prediction From the Sensor Inputs
fr=open('P_INFO.txt', 'r')
bp=open('BP.txt','r')
fp=open('spo2.txt','r')
ci=open('CI.txt','w')
for line in fr:
    field=line.split(",")
    gender=field[0]
    age=float(field[1])
    if(gender=='Male'):
        gender=1
    else:
        gender=0
        
for l1 in bp:
    field2=l1.split(',')
    SBP=(float(field2[0]))
    DBP=(float(field2[1]))
for l in fp:
    field1=l.split(',')
    PR=(float(field1[0]))
    BOL=(float(field1[1]))
    BT=(float(field1[2]))
    pred_args=[age,gender,BT,PR,BOL,SBP,DBP]
    pred_args_arr=np.array(pred_args)
    pred_args_arr=pred_args_arr.reshape(1,-1)
    #Writing predicted Critical INdex value
    model_prediction=ml_model.predict(pred_args_arr)
    model_prediction=round(float(model_prediction),2)
    ci.write(str(model_prediction))
    ci.write('\n')

