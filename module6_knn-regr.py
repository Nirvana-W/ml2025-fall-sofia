import numpy as np

class KNNRegressor:
    def __init__(self, k):
        self.k = k
        self.X_train = None
        self.y_train = None

    def fit(self, X, y):
        self.X_train = np.array(X, dtype=float)
        self.y_train = np.array(y, dtype=float)

    def predict(self, X_input):
        if self.k > len(self.X_train):
            raise ValueError("k cannot be greater than the number of training points.")

        distances = np.abs(self.X_train - X_input)
        nearest_idx = np.argsort(distances)[:self.k]
        return np.mean(self.y_train[nearest_idx])

def main():
    N = int(input("Enter N (number of points): "))
    if N <= 0:
        print("N must be a positive integer.")
        return

    k = int(input("Enter k (number of neighbors): "))
    if k <= 0:
        print("k must be a positive integer.")
        return

    X_points = []
    y_points = []

    print(f"Enter {N} points (x and y values one by one):")
    for i in range(N):
        x_val = float(input(f"x{i+1}: "))
        y_val = float(input(f"y{i+1}: "))
        X_points.append(x_val)
        y_points.append(y_val)

    knn = KNNRegressor(k)
    knn.fit(X_points, y_points)

    X_input = float(input("Enter X to predict Y: "))

    try:
        y_pred = knn.predict(X_input)
        print(f"Predicted Y for X = {X_input}: {y_pred}")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
