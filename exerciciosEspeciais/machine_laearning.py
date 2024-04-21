# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Generate some synthetic data
# np.random.seed for reproducibility
np.random.seed(0)
X = 2.5 * np.random.randn(100) + 1.5   # Array of 100 values with mean = 1.5, stddev = 2.5
res = 0.5 * np.random.randn(100)       # Generate 100 residual terms
y = 2 + 0.3 * X + res                  # Actual values of Y

# Reshape X to be the matrix (100, 1)
X = X.reshape(-1, 1)

# Create a linear regression model
model = LinearRegression()

# Fit the model
model.fit(X, y)

# Predict y from the data
y_pred = model.predict(X)

# Plotting the results
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, y_pred, color='red', label='Fitted line')
plt.title('Linear Regression')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# Print the coefficients
print(f"Coefficient: {model.coef_[0]}")
print(f"Intercept: {model.intercept_}")

# Print the performance metrics
print("Mean squared error: %.2f" % mean_squared_error(y, y_pred))
print("Coefficient of determination (R^2): %.2f" % r2_score(y, y_pred))
