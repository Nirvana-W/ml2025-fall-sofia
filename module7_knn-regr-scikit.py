import numpy as np
from sklearn.neighbors import KNeighborsRegressor
from sklearn.exceptions import NotFittedError

N = int(input("Enter N (number of points): "))

k = int(input("Enter k: "))

data = np.zeros((N, 2), dtype=float)

print("Enter the points:")
for i in range(N):
    x = float(input(f"Point {i+1} - x: "))
    y = float(input(f"Point {i+1} - y: "))
    data[i] = [x, y]

X_train = data[:, 0].reshape(-1, 1)
y_train = data[:, 1]

x_query = float(input("Enter X to predict Y using k-NN regression: "))
x_query = np.array([[x_query]])

if k > N:
    print("Error: k cannot be greater than N.")
else:
    model = KNeighborsRegressor(n_neighbors=k)
    model.fit(X_train, y_train)

    y_pred = model.predict(x_query)[0]

    print(f"\nPredicted Y for X={x_query[0][0]} using k-NN Regression: {y_pred}")

    variance = np.var(y_train)
    print(f"Variance of labels in training data: {variance}")
