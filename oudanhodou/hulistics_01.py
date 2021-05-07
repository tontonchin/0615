
import math
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

def kakudo(fa=3,  alpha0=pi/4):
    Dmax = 5
    def objective_function(theta, fa=3,  alpha0=pi/4):
        return  Dmax*2 + fa**2 -2* Dmax*fa*math.cos(math.radians(alpha0-theta))
    min = optimize.fminbound(objective_function,-pi/4,pi/4)
    print(min)
    print(math.degrees(min))
    return min




def kakudo_kai(fa,  alpha0):
    Dmax = 10
    def objective_function(theta):
        return  Dmax*2 + fa**2 -2* Dmax*fa*math.cos(math.radians(alpha0-theta))
    min = optimize.fminbound(objective_function,0,pi)

    #print(min)
    #print(math.degrees(min))
    return min

def kakudo_kai_sita(fa,  alpha0 , beta, ganma):
    print("いぬかいたい",math.degrees(beta),math.degrees(ganma))
    Dmax = 10
    def objective_function(theta):
        return  Dmax*2 + fa**2 -2* Dmax*fa*math.cos(math.radians(alpha0-theta))
    min1 = optimize.fminbound(objective_function,0, beta)
    min2 = optimize.fminbound(objective_function,ganma, pi)
    print("min1",min1,"min2",min2)
    #print(min)
    #print(math.degrees(min))
    min_1 = alpha0 - abs(alpha0- min1)
    min_2 = alpha0 - abs(alpha0- min2)
    if min_1 >= min_2:
        min = min1
    else:
        min = min2
    print("ぼくどらえもんmin1min2",math.degrees(min1),math.degrees(min2))
    print("わたしどらみちゃんminよ", math.degrees(min))

    return min


def kakudo_kai_ue(fa,  alpha0):
    Dmax = 10
    def objective_function(theta):
        return  Dmax*2 + fa**2 -2* Dmax*fa*math.cos(math.radians(alpha0-theta))
    min = optimize.fminbound(objective_function, pi, 2*pi)
    #print(min)
    #print(math.degrees(min))
    return min

def kakudo_kai_ue2(fa,  alpha0, beta, ganma):
    Dmax = 10
    def objective_function(theta):
        return  Dmax*2 + fa**2 -2* Dmax*fa*math.cos(math.radians(alpha0-theta))
    min1 = optimize.fminbound(objective_function,0, beta)
    min2 = optimize.fminbound(objective_function,ganma, pi)
    print("min1",min1,"min2",min2)
    #print(min)
    #print(math.degrees(min))
    min_1 = alpha0 - abs(alpha0- min1)
    min_2 = alpha0 - abs(alpha0- min2)
    if min_1 >= min_2:
        min = min1
    else:
        min = min2
    print("ぼくどらえもんmin1min2",math.degrees(min1),math.degrees(min2))
    return min





if __name__ == "__main__":
    kakudo()
    kakudo_kai()
    kakudo_kai_ue()