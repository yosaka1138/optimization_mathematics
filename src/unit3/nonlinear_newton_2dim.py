#coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x, y):
    return 5 - 10*(x - 1) ** 2 - 20*(y - 25) ** 2

def fx(x, y):
    return -20 * x + 20

def fxx(x, y):
    return -20

def fy(x, y):
    return -40 * y + 1000

def fyy(x, y):
    return -40

def fxy(x, y):
    return 0

def newton(init):
    init_tmp = init[:]
    eps = 1e-8
    while True:
        dx, dy = init_tmp[:]
        H = np.array([[fxx(init_tmp[0], init_tmp[1]), fxy(init_tmp[0], init_tmp[1])], 
                      [fxy(init_tmp[0], init_tmp[1]), fyy(init_tmp[0], init_tmp[1])]])
        H_inv = np.linalg.inv(H)
        nabla_f = np.array([fx(init_tmp[0], init_tmp[1]), fy(init_tmp[0], init_tmp[1])])
        init_tmp = init_tmp - np.dot(H_inv, nabla_f)
        if np.sqrt((dx - init_tmp[0])**2 + (dy - init_tmp[1])**2) < eps:
            break
        # print(*init_tmp)
    return init_tmp

def plot_contour(calc_xy):
    calc_x, calc_y = calc_xy
    x = np.linspace(-50, 100, 200)
    y = np.linspace(-50, 100, 200)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.set_xlabel("x", fontsize = 16)
    ax.set_ylabel("y", fontsize = 16)
    ax.set_zlabel("z", fontsize = 16)
    # ax.plot_surface(X, Y, Z, cmap="summer")
    ax.plot_wireframe(X, Y, Z, cmap="Accent", lw=0.3)
    ax.scatter(calc_x, calc_y, f(calc_x, calc_y), marker="*", s=100, c="red")
    plt.show()


def main():
    init_x, init_y = -3.0, -5.0
    init = [init_x, init_y]
    ans = newton(init)
    print(*ans)
    print("f(optim_x, optim_y) =", f(ans[0], ans[1]))
    plot_contour(ans)

if __name__ == "__main__":
    main()