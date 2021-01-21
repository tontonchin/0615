
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
    Dmax = 10
    def objective_function(theta, fa=3,  alpha0=pi/4):
        return  Dmax*2 + fa**2 -2* Dmax*fa*math.cos(math.radians(alpha0-theta))
    min = optimize.fminbound(objective_function,-pi/4,pi/4)
    print(min)
    print(math.degrees(min))
    return min




def kakudo_kai(fa=3,  alpha0=pi/4):
    Dmax = 10
    def objective_function(theta):
        return  Dmax*2 + fa**2 -2* Dmax*fa*math.cos(math.radians(alpha0-theta))
    min = optimize.fminbound(objective_function,0,pi)
    #print(min)
    #print(math.degrees(min))
    return min

a = kakudo_kai()
print(a,type(a))




def kakudo_kai_ue(fa=3,  alpha0=pi/4):
    Dmax = 10
    def objective_function(theta):
        return  Dmax*2 + fa**2 -2* Dmax*fa*math.cos(math.radians(alpha0-theta))
    min = optimize.fminbound(objective_function,(pi/2+pi/4),(3*pi/2+pi/4))
    min = optimize.fminbound(objective_function, pi, 2*pi)
    #print(min)
    #print(math.degrees(min))
    return min




if __name__ == "__main__":
    kakudo()
    kakudo_kai()
    kakudo_kai_ue()