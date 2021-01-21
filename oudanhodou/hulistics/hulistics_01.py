import math
import numpy as np
from mesa import Agent, Model
import math
from math import sqrt
import random
from mesa.time import RandomActivation
import matplotlib.pyplot as plt
from scipy import optimize


pi = math.pi

""""
def objective_function(theta, fa=3,  alpha0=pi/4):
    '''目的関数'''
    return 10**2 + fa**2 -2*10*fa*math.cos(math.radians(alpha0-theta))




min = optimize.brent(objective_function)
print(min)
print(math.degrees(min))
"""

def kakudo( fa=3,  alpha0=pi/4):
    Dmax = 10
    def objective_function(theta, fa=3,  alpha0=pi/4):
        return  Dmax*2 + fa**2 -2* Dmax*fa*math.cos(math.radians(alpha0-theta))
    min = optimize.fminbound(objective_function,-pi,pi)
    print(min)
    print(math.degrees(min))
    return min




if __name__ == "__main__":
    kakudo()