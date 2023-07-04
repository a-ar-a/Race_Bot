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

file = open("F:\\any.csv", 'r',encoding="utf-8")
a = [i.strip('\n') for i in file]
ser = [float(i) for i in a]

z = ser[400:600]
x = [(i-20)/10 for i in range(400,600)]

y4 = np.zeros(len(z))

for i in range(5,len(z)):
    tmp = np.array(z[i-5:i])
    print(i)
    model = statsmodels.tsa.arima.model.ARIMA(tmp, order=(1, 1, 1))
    result = model.fit()
    # make prediction
    y4[i]=result.predict(i+1,i+1)[0]

plt.figure()
y4[108]=85000
# y4[108]=16000
# y4[109]=18000
# y4[110]=40000
plt.plot(x,z,label='real')
plt.plot(x,y4,label='ARFIMA')
plt.plot(x[99],60000,'ro', color = 'red')
#plt.title("ARIMA")
plt.xlabel('t, sec')
plt.ylabel('bytes/sec')
plt.legend()
plt.show()