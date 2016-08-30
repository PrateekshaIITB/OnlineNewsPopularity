
import pandas as pd # now you can refer to pandas library as 'pd' from here on.
import numpy as np

df = pd.read_csv('train_data.csv', header=0)

td = pd.read_csv('test_data.csv', header=0)
from sklearn import linear_model

#train_data=df.ix[0:500,]
#validate_data=df.ix[500:,]

lr=linear_model.LinearRegression()
trainx=df.ix[:,2:60]
trainy=df.ix[:,60]
lr.fit(trainx,trainy)

print("w values for the linear model",lr.coef_)

testx=td.ix[:,2:60]
#testy=td.ix[:,60]
ypredicted=lr.predict(testx)
predicted_values=pd.DataFrame(ypredicted)
#print(predicted_values.head())

#def fun1(x):
 #   if x>0.5:
  #      return 1
   # else:
   #     return 0

#predicted_labels = predicted_values[0].apply(fun1)

#print(predicted_labels.head())
#print(testy.head())
predicted_values.to_csv("output1lr.csv", index_label = ["id"], header =["shares"])