"""このプログラムでは"""


import math
import numpy as np
from mesa import Agent, Model
import math
from math import sqrt
import random
from mesa.time import RandomActivation
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def func_dydt(y, t):
    dydt = -y

    return dydt

#2d可視化
def plot2d(t_list, y_list, t_label, y_label):
    plt.xlabel(t_label)  #x軸の名前
    plt.ylabel(y_label)  #y軸の名前
    plt.grid()  #点線の目盛りを表示
    plt.plot(t_list, y_list)

    plt.show()

t_list = np.linspace(0.0, 10.0, 1000)
y_init = 1.0  #初期値
y_list = odeint(func_dydt, y_init, t_list)
#print(y_list)

#3d可視化
def plot3d(t_list, var_list):
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.set_xlabel("$x$")  #x軸の名前
    ax.set_ylabel("$y$")  #y軸の名前
    ax.set_zlabel("$z$")  #z軸の名前
    ax.plot(var_list[:, 0], var_list[:, 1], var_list[:, 2])

    plt.show()


pi = math.pi
def hito_sesyoku(a=(math.pi)/4):
    ri = 60/320
    rj = 60/320
    nij= np.array([(-1)*math.cos(a), (-1)*math.sin(a)])
    return 1*9.8*(ri + rj - 5) * nij

c = hito_sesyoku()
print(c)

def kabe_sessyoku(a=(math.pi)/4):
    ri = 60/320
    nij = np.array([(-1)*math.cos(a), (-1)*math.sin(a)])
    return 5000*9.8*(ri- 3) * nij

#作成したい方程式
def func_hulistics_2(vdes_x, t,N=10):
    #dvdt = (vdes-vi)/tau +k*g*(ri+rj-dij)  +k*g*()
    #x方向のベクトル
    pi = math.pi
    vii =np.array([vi[0]*math.cos(pi/4), vi[1]*math.sin(pi/4)])
    kabe = 0
    hito = 0

    def hito_sesyoku(a=(math.pi) / 4):
        ri = 60 / 320
        rj = 60 / 320
        nij = np.array([(-1) * math.cos(a), (-1) * math.sin(a)])
        return 5000 * 9.8 * (ri + rj - 5) * nij

    def kabe_sessyoku(a=(math.pi) / 4):
        ri = 60 / 320
        nij = np.array([(-1) * math.cos(a), (-1) * math.sin(a)])
        return 5000 * 9.8 * (ri - 3) * nij
    for i in range(N):
        hito += hito_sesyoku()/60
        kabe += kabe_sessyoku()/60
    dvdt = ((vdes_x-vii)/0.5)+hito + kabe
    #print(dvdt)
    return dvdt


""""
t_list = np.linspace(0.0, 10.0, 1000)
vi = np.array([1.3, 0] ) #初期値
vi_list = odeint(func_hulistics_2, vi, t_list)

print(vi_list)

a = kabe_sessyoku()
print(a)

"""
vi = np.array([1.3, 0] )

#plot2d(t_list, vi_list[:, 0], "$t$", "$v(t)$")
#plot2d(t_list, vi_list[5, 0], "$t$", "$y(t)$")


def func_hulistics_2_kai(vdes=np.array([1.3, 0]),N=10):
    #dvdt = (vdes-vi)/tau +k*g*(ri+rj-dij)  +k*g*()
    #x方向のベクトル
    pi = math.pi
    vii =np.array([vi[0]*math.cos(pi/4), vi[1]*math.sin(pi/4)])
    kabe = 0
    hito = 0

    def hito_sesyoku(a=(math.pi) / 4):
        ri = 60 / 320
        rj = 60 / 320
        nij = np.array([(-1) * math.cos(a), (-1) * math.sin(a)])
        return 5 * 9.8 * (ri + rj - 5) * nij

    def kabe_sessyoku(a=(math.pi) / 4):
        ri = 60 / 320
        nij = np.array([(-1) * math.cos(a), (-1) * math.sin(a)])
        return 5 * 9.8 * (ri - 3) * nij
    for i in range(2):
        hito += hito_sesyoku()/60
    for i in range(1):
        kabe += kabe_sessyoku()/60
    dvdt = ((vdes-vii)/0.5)+hito + kabe
    #print(dvdt)
    return dvdt

b = func_hulistics_2_kai()
print(b)

#if __name__ == "__main__":