import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model

# Generate a function
x = np.random.uniform(1,100,1000)  # 1000 random numbers between 1 and 100
y = np.log(x)   # function y is lograthim of x
y = y + np.random.normal(0,0.3,1000)    # add random noise
# get the regression object
#regression = linear_model.LinearRegression()
#regression.fit(x,y)

# fit a curve
# curve = np.polyfit(x,y,10)
# xfit = np.linspace(-10, 120, 100)
# yfit = np.log(xfit)

# Training
x = np.reshape(x,(1000,1))
rf = RandomForestClassifier()
rf.fit(x, y)

# Testing
xfit = np.linspace(-10, 120, 1000)
a, = xfit.shape
xfit = np.reshape(xfit,(a,1))
yfit = rf.predict(xfit)

plt.scatter(xfit,yfit)
plt.scatter(x,y)
plt.xlabel('points')
plt.ylabel('log')
plt.show()
