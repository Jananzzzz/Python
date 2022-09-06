#from array import array
#from pyexpat import model
from array import array
import numpy as np
from sklearn.linear_model import LinearRegression
'''
x = np.array([1, 2, 3, 4, 5]).reshape((-1, 1))
'''
y = np.array([1, 2, 3, 4, 5])

# x now is the same as below 
x = np.array([[1], [2], [3], [4], [5]])



model = LinearRegression()
model.fit(x, y)
#LinearRegression()
#above two lines equal to:
# model = LinearRegression().fit(x, y)

#step4: getting the result:
CoefficientOfDetermination = model.score(x, y)
print(f"Coefficient of Determination: {CoefficientOfDetermination}")
print(f"Intercept: {model.intercept_}")
print(f"Slope: {model.coef_}")
#notice that intercept_ is a scalar while coef is an array.
#in scikit-learn, by convention, a trailing underline indicates that an attribute is estimated.

prediction_s1 = model.predict(x)
print(f"Predict y of each x is: {prediction_s1}")
#above is the same as below:
prediction_s2 = model.intercept_ + model.coef_ * x
print(f"predict y of each x:\n {prediction_s2}")
#we can change the result format by transpose x like below: 
prediction_s3 = model.intercept_ + model.coef_ * x.reshape(-1)
print(f"predict y of each x:\n {prediction_s3}")
#x.reshape(-1) is the same as x.ravel() and x.flatten

x_new = np.arange(5).reshape((-1, 1))
y_new = model.predict(x_new)
print(y_new)
# arange(5) is 0, 1, 2, 3, 4

#Multiple linear regresion
x1 = [
  [0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]
]
y1 = [4, 5, 20, 14, 32, 22, 38, 43]
x1, y1 = np.array(x1), np.array(y1)

print(x1, y1) 
model2 = LinearRegression().fit(x1, y1)
multi_predict = model2.predict(x1)
print(multi_predict)
print(model2.score(x1, y1))


x1new = np.arange(10).reshape(-1, 2)
print(x1new)
print(model2.predict(x1new))




# Polynomial Regression With scikit-learn
from sklearn.preprocessing import PolynomialFeatures
x3 = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y3 = np.array([15, 11, 2, 8, 25, 32])

"""
transformer = PolynomialFeatures(degree = 2, include_bias = False)
transformer.fit(x3)

x_ = transformer.transform(x3)

print(x_)

#create a polynomial model

polymodel = LinearRegression().fit(x_, y3)
R = polymodel.score(x_, y3)
print(f"Coefficient of determination is: {R}")

print(polymodel.intercept_)
print(polymodel.coef_)
"""

# below is a transformer with bias which is a intercept term

transformer = PolynomialFeatures(degree = 2, include_bias = True)
transformer.fit(x3)
x_ = transformer.transform(x3)

print(x_)
# then create a model without additional intercept term

polymodel = LinearRegression(fit_intercept = False).fit(x_, y3)
R = polymodel.score(x_, y3)
print(f"Coefficient of determination is: {R}")
print(polymodel.intercept_)
print(polymodel.coef_)

# below is the multi-variable-multi-term regression
'''
# Step 1: Import packages and classes
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Step 2a: Provide data
x = [
  [0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]
]
y = [4, 5, 20, 14, 32, 22, 38, 43]
x, y = np.array(x), np.array(y)

# Step 2b: Transform input data
x_ = PolynomialFeatures(degree=2, include_bias=False).fit_transform(x)

# Step 3: Create a model and fit it
model = LinearRegression().fit(x_, y)

# Step 4: Get results
r_sq = model.score(x_, y)
intercept, coefficients = model.intercept_, model.coef_

# Step 5: Predict response
y_pred = model.predict(x_)
'''























