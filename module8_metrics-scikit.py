import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    N = int(input("Enter the number of points (N): "))

    X = np.zeros(N, dtype=int)
    Y = np.zeros(N, dtype=int)

    for i in range(N):
        x = int(input(f"Enter ground truth class for point {i+1} (0 or 1): "))
        y = int(input(f"Enter predicted class for point {i+1} (0 or 1): "))
        X[i] = x
        Y[i] = y

    precision = precision_score(X, Y)
    recall = recall_score(X, Y)

    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()
