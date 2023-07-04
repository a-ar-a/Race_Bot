# ARIMA example
import statsmodels
from statsmodels.graphics.tsaplots import plot_predict
from statsmodels.tsa.arima.model import ARIMA
#import statsmodels.api as sm
import warnings
# import statsmodels.api as sm
import warnings

import matplotlib.pyplot as plt
import statsmodels
from statsmodels.tsa.arima.model import ARIMA

warnings.filterwarnings("ignore")
# contrived dataset
# ARMA example
from random import random
# contrived dataset

import numpy as np
import random
import matplotlib.pyplot as plt

def mape(actual, pred):
    actual, pred = np.array(actual), np.array(pred)
    return np.mean(np.abs((actual-pred)/actual)) * 100
# 
# file = open("E:\\test9.csv", 'r', encoding='utf-8')
# a = [i.strip('\n') for i in file]
# serial = [float(i) for i in a]
# 
# z = serial[1090:1200]

a = 0
b = 100
m = 8
n = 2**m
print(n)
H = 0.8

x = np.zeros(n)
y = np.zeros(n)
x[0] = a
y[0] = 100
y[n-1] = 100
hx = (b-a)/n
for i in range(1,n):
    x[i] = x[i-1]+hx

for i in range(m-1):
    w = n/(2**i)
    for j in range(2**i-1):
        left = int(w*j)
        right = int(w*(j+1))
        #print(left)
        #print(right)
        r = (x[right]-x[left])/2
        d = r**H
        h = d*random.random()
        mid = int((left+right)/2)
        #print(mid)
        y[mid] = (y[left]+y[right])/2+h

for i in range(len(y)):
    if y[i] == 0:
        y[i] = random.random() * 10

x1 = np.zeros(int(len(y)/2)-1)
y1 = np.zeros(int(len(y)/2)-1)

ind = -1
for i in range(int(len(y)/2), len(y)-1):
    ind +=1
    y1[ind] = y[i]
    x1[ind] = ind+1
    if y[i] == 0:
        y1[ind] = random.random() * 10



#data = [x+random() for x in range(1, 100)]
data = x1
# fit model
model = statsmodels.tsa.arima.model.ARIMA(data, order=(1,1,2))
result = model.fit()
# make prediction
print(result.predict(127,127))
y2 = np.zeros(len(y1))

for i in range(10,len(x1)):
    tmp = np.array(y1[i-10:i:1])

    print(i)
    model = statsmodels.tsa.arima.model.ARIMA(tmp, order=(0, 0, 1))
    result = model.fit()
    # make prediction
    y2[i]=result.predict(i+1,i+1)[0]

print(y1)

y3 = np.zeros(len(y1))

for i in range(10,len(x1)):
    tmp = np.array(y1[i-10:i:1])
    for j in range(int(len(tmp)/2)):
        tmp[j] = tmp[j]*0.3
    print(i)
    model = statsmodels.tsa.arima.model.ARIMA(tmp, order=(0, 0, 1))
    result = model.fit()
    # make prediction
    y3[i]=result.predict(i+1,i+1)[0]

print(y1)

y4 = np.zeros(len(y1))

for i in range(10,len(y1)):
    tmp = np.array(y1[i-10:i:1])
    print(i)
    model = statsmodels.tsa.arima.model.ARIMA(tmp, order=(1, 1, 1))
    result = model.fit()
    # make prediction
    y4[i]=result.predict(i+1,i+1)[0]

plt.figure()

plt.plot()
plt.plot(x1,y1,label='real')
plt.plot(x1,y2,label='MA')
#plt.title("MA")
plt.xlabel('time')
plt.ylabel('value')
plt.legend()
plt.show()

plt.plot()
plt.plot(x1,y1,label='real')
plt.plot(x1,y3,label='WMA')
#plt.title("WMA")
plt.xlabel('time')
plt.ylabel('value')
plt.legend()
plt.show()

plt.plot(x1,y1,label='real')
plt.plot(x1,y4,label='ARIMA')
plt.title("ARIMA")
plt.xlabel('time')
plt.ylabel('value')
plt.legend()
plt.show()

res = 0
for i in range(10,len(y1),1):
    res = res + (abs(y1[i]-y2[i])/y1[i])
res = res/(len(y1)-10)
print(res*100)

res = 0
for i in range(10,len(y1),1):

    res = res + abs(y1[i]-y3[i])/y1[i]
res = res/(len(y1)-10)
print(res*100)

res = 0
for i in range(10,len(y1),1):
    res = res + abs(y1[i]-y4[i])/y1[i]
res = res/(len(y1)-10)
print(res*100)

print(mape(y1[10:],y2[10:]))
print(mape(y1[10:],y3[10:]))
print(mape(y1[10:],y4[10:]))

print(mape(y2[10:],y1[10:]))
print(mape(y3[10:],y1[10:]))
print(mape(y4[10:],y1[10:]))