#coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 + 5*x**2 + x + 1

def f_prime(x):
    return 3*x**2 + 10*x + 1

def f_double_prime(x):
    return 6*x + 10

def newton(x):
    eps = 1e-8
    # x = - 5.0
    idx = 0
    print("初期値:", x)
    while True:
        dx = x
        x = x - f_prime(x) / (f_double_prime(x) + 1e-10)
        if abs(x - dx) < eps:
            break
        # if idx % 5 == 0:
            # print(dx, x)
    return x


def plot_function(calc_x):
    x = np.linspace(-5, 1, 100)
    y = f(x)
    plt.plot(x, y, c="blue")
    plt.scatter(calc_x, f(calc_x), marker="*", s=100, c="red")
    plt.grid(True)
    plt.show()

def main():
    init_x = 5.0
    calc_x = newton(init_x)
    print("極値を取るx:", calc_x)
    plot_function(calc_x)


if __name__ == "__main__":
    main()