import math
import numpy as np
from mesa import Agent, Model
import math
from math import sqrt
import random
from mesa.time import RandomActivation
import matplotlib.pyplot as plt
#周囲のエージェント(視野角の中にある)を確認するプログラムを作成する
#具体的には，エージェント間の全ての距離を計算して　Dmaxに入るかどうかで場合わけ
#その後，それぞれのエージェント同士の角度から傾きとして得られる傾きから-tanA =< 必要なもの =< =tanA以外のものを採用し，残す
#それで残ったものを各エージェントの計算に用いるものとして採用する
#エージェントの集団の配列
agents = np.array([[1, 2],
                            [8, 1],
                            [3, 3],
                            [3, 4],
                            [4, 0],
                            [5, 2],
                            [5, 23],
                            [2, 12],
                            [1, 8],
                            [7, 3],
                          ])

#agents_i = np.zeros((10,2))


print("#############################################")

def syuui1(agents,N):
    Dmax = 10
    oobako = np.zeros((N,N))
    ootan = np.zeros((N, N))
    agents_i = np.zeros((N,2))
    for i in range(N):
        #if i > 0:
         #   print(i-1, "番目", tan, "つかれた")
          #  print("はこは",hako)
        a = agents[i, 0]
        b = agents[i, 1]
        for j in range(N):
            agents_i[j, 0] = a
            agents_i[j, 1] = b
        # print(agents_i)
        matome = agents - agents_i
        #print(matome)
        hako = np.zeros(N)
        for k in range(N):
            hako[k] = np.linalg.norm(matome[k])
        # print(hako)

        for l in range(N):
            # print(hako[l])
            if hako[l] >= 10:
                matome[l, 0] = 0
                matome[l, 1] = 0
                hako[l] = 0
                oobako[i,l] = hako[i]
        # print(matome)

        pi = math.pi
        tan_sip = math.tan(math.radians(45))
        tan_sim = -1 * tan_sip
        # print(tan_sip, tan_sim)
        tan = np.zeros(N)
        for j in range(N):
            if matome[j, 0] != 0 and matome[j, 1] != 0:
                tan[j] = matome[j, 1] / matome[j, 0]
        for u in range(N):
            #oobako[i, u] = hako[u]
            if not tan[u] >= tan_sim and tan[u] <= tan_sip:
                tan[u] = False
                hako[u] = False
            oobako[i, u] = hako[u]
            ootan[i, u] = tan[u]
        # print(i,"番目",tan,"つかれた")
        #print(i , "番目", tan, "つかれた")
        #print("はこは", hako)
    #print("oobakoは",oobako)
    #print( "ootanは",ootan)
    return oobako


def syuui2(agents, N):
    Dmax = 10
    oobako = np.zeros((N,N))
    ootan = np.zeros((N, N))
    agents_i = np.zeros((N, 2))
    for i in range(N):
        #if i > 0:
         #   print(i-1, "番目", tan, "つかれた")
          #  print("はこは",hako)
        a = agents[i, 0]
        b = agents[i, 1]
        for j in range(N):
            agents_i[j, 0] = a
            agents_i[j, 1] = b
        # print(agents_i)
        matome = agents - agents_i
        #print(matome)
        hako = np.zeros(N)
        for k in range(N):
            hako[k] = np.linalg.norm(matome[k])
        # print(hako)

        for l in range(N):
            # print(hako[l])
            if hako[l] >= 10:
                matome[l, 0] = 0
                matome[l, 1] = 0
                hako[l] = 0
                oobako[i,l] = hako[i]
        # print(matome)

        pi = math.pi
        tan_sip = math.tan(math.radians(45))
        tan_sim = -1 * tan_sip
        # print(tan_sip, tan_sim)
        tan = np.zeros(N)
        for j in range(N):
            if matome[j, 0] != 0 and matome[j, 1] != 0:
                tan[j] = matome[j, 1] / matome[j, 0]
        for u in range(N):
            #oobako[i, u] = hako[u]
            if not tan[u] >= tan_sim and tan[u] <= tan_sip:
                tan[u] = False
                hako[u] = False
            oobako[i, u] = hako[u]
            ootan[i, u] = tan[u]
        # print(i,"番目",tan,"つかれた")
        #print(i , "番目", tan, "つかれた")
        #print("はこは", hako)
    #print("oobakoは",oobako)
    print( "ootanは",ootan)
    return ootan

"""
a = syuui1(agents)
b = syuui2(agents)
a1 = a[0]
b1 = b[0]
b2 = b[1]
b3 = b[2]
b4 = b[3]
b5 = b[4]
b6 = b[5]
b7 = b[6]
b8 = b[7]
b9 = b[8]

print("%%%%%*&%*&%*&%*&%*&(*%&*(%&*(&%*(&%*(&%*&%(")
print("a1は",a1)
print(b1)


#ぶつかるかぶつからないかどうかの判定
tana = math.tan(math.pi/4)
for i in b1:
    #print("これは",i)
    if tana - 0.3 < i and i < tana + 0.3:
        print("ぶつかる")
    else:
        print("ぶつからない")

for i in b2:
    #print("これは",i)
    if tana - 0.3 <= i and i <= tana + 0.3:
        print("ぶつかる")
    else:
        print("ぶつからない")

for i in b3:
    #print("これは",i)
    if tana - 0.3 < i and i < tana + 0.3:
        print("ぶつかる")

for i in b4:
    #print("これは",i)
    if tana - 0.3 < i and i < tana + 0.3:
        print("ぶつかる")

for i in b5:
    #print("これは",i)
    if tana - 0.3 < i and i < tana + 0.3:
        print("ぶつかる")
"""

print("_____________________________________________________________________")

#これを関数に直す

def hantei(agents_kaku):
    tana = math.tan(math.pi / 4)
    for i in agents_kaku:
        if (tana - 0.3) <= i:
            if i < (tana + 0.3):
                return True


def hankai(agents_kaku):
    tana = math.tan(math.pi / 4)
    for i in agents_kaku:
        if (tana - 0.3) <= i and i < (tana + 0.3):
            return True
        else:
            return False

def han_kyori(agent_kaku,num=10):
    tana = math.tan(math.pi / 4)
    butukaru = np.array([])

    for i in range(num):
        if (tana - 0.3) <= agent_kaku[i] and agent_kaku[i] < (tana + 0.3):
            butukaru = np.append(butukaru,i)
    return butukaru






#tehu = hantei(b1)
#print(tehu)

#unko = hankai(b4)
#print(unko)


#print(han_kyori(b1))
#print(han_kyori(b2))
#print(han_kyori(b3))
#print(han_kyori(b4))
#print(han_kyori(b5))
#print(han_kyori(b6))
#print(han_kyori(b7))
#print(han_kyori(b8))

print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
if __name__ == "__main__":
    syuui1(agents)
    syuui2(agents)
