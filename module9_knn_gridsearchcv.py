import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

def read_pairs(num_pairs, dataset_name):
    X = np.zeros((num_pairs, 1), dtype=float) 
    y = np.zeros(num_pairs, dtype=int)
    print(f"Enter {num_pairs} pairs for {dataset_name}:")
    for i in range(num_pairs):
        X[i, 0] = float(input(f"Pair {i+1} - x: "))
        y[i] = int(input(f"Pair {i+1} - y: "))
    return X, y

N = int(input("Enter number of training pairs N: "))
X_train, y_train = read_pairs(N, "training set")
M = int(input("Enter number of test pairs M: "))
X_test, y_test = read_pairs(M, "test set")
param_grid = {'n_neighbors': np.arange(1, 11)}
knn = KNeighborsClassifier()
grid = GridSearchCV(knn, param_grid, cv=5)
grid.fit(X_train, y_train)
best_k = grid.best_params_['n_neighbors']
best_knn = grid.best_estimator_
test_accuracy = best_knn.score(X_test, y_test)

print(f"\nBest k: {best_k}")
print(f"Test accuracy: {test_accuracy:.4f}")
