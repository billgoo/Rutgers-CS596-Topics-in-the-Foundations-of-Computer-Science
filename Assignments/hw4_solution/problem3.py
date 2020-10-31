import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.scale as sc

# numpy.random.normal(loc=0.0, scale=1.0, size=(m, n, k))
LENGTH = 5
THETA_STAR = np.array([25, 22, 16, 132, 66])
MU = 0.01

def generate_samples(t, length):
    X = np.random.normal(size=(t, length))
    W = np.random.normal(loc=0.0, scale=0.1, size=t)
    # print(X)
    # print(W)
    Y = np.array([np.dot(THETA_STAR.transpose(), X[i]) + W[i] for i in range(t)])

    return Y, X, W


def lms(Y, X, mu):
    theta = np.array([0.0 for _ in range(5)])
    e = []

    for t in range(Y.size):
        temp = theta
        theta = temp + np.dot((mu * (Y[t] - np.dot(temp.transpose(), X[t]))), X[t])
        # theta = theta + np.dot((MU * (Y[t] - np.dot(theta.transpose(), X[t]))), X[t])
        e.append(np.linalg.norm(theta - THETA_STAR) ** 2)

    return e, theta



if __name__ == "__main__":
    t = 2600
    Y, X, W = generate_samples(t, LENGTH)
    iter_ = [i for i in range(Y.size)]

    # c is for question c) with higher mu and d with mu / 2 in the question d)
    error_c, theta_c = lms(Y, X, MU)
    error_d, theta_d = lms(Y, X, MU/2)

    print(theta_c)
    # print(min(error_c), error_c[-1])
    print(theta_d)
    # print(min(error_d), error_d[-1])
    
    plt.figure(figsize=(13,8))
    plt.plot(iter_, error_c, color='r', linestyle='-', label="mu = 0.01")
    plt.plot(iter_, error_d, color='b', linestyle='-.', label="mu = 0.005")
    plt.ylabel('||theta_T - theta_star||^2')
    plt.xlabel('No. of iterations')
    plt.semilogy(error_c)
    plt.semilogy(error_d)
    plt.legend()
    plt.show()

    print("end")
