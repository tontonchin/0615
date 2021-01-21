import numpy as np
from mesa import Agent, Model
import math
import random
from mesa.time import SimultaneousActivation
import matplotlib.pyplot as plt
#from  hulistics.hulistics_01 import kakudo
from hulistics_01 import kakudo, kakudo_kai
#from hulistics.hulistics_02 import plot2d, hito_sesyoku, kabe_sessyoku, func_hulistics_2
#from hulistics.syuuino import syuui1,syuui2,hankai,han_kyori
from mesa.space import ContinuousSpace
from scipy import optimize


"""歩行者エージェントを二つのクラスに分ける，理由としては名古屋大学の分析結果などを用いて，"""


class Hokousya_sita(Agent):
    "人ですこれはmoussaidのヒューリスティクスにしたがう"

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        # これは設定されたパラメータ，一様である
        self.tyon = 0.5
        self.siyakaku = math.pi/4
        self.dmax = 10
        self.K = 5
        #self.a = (math.pi) / 2
        #self.vi = np.array([1.3,0])
        #self.vdes = np.array([1.3,0])*np.array([math.cos(self.a), math.sin(self.a)])
        # これは，歩行者エージェントごとに異なるもの，初期位置である
        self.iti_x = round(random.randrange(0, 10)*random.random(),3)
        self.iti_y = round(random.randrange(0, 5)*random.random(),3)

        self.a =  (math.pi) / 2
        self.iti = np.array([self.iti_x, self.iti_y])
        self.vi = np.array([1.3, 0])
        self.vdes = np.array([1.3, 0]) * np.array([math.cos(self.a), math.sin(self.a)])
        self.mokutekiti_0 = np.array([self.iti_x, self.iti_y + 30 ])
        self.m = 60


    def step(self):

        "ここで関数を用いる"
        "まず，周囲の位置情報を確認する"
        #pass
        #周囲のエージェントとの距離の確認
        plt.scatter(self.iti[0], self.iti[1])

        if self.katikan == 1:
            self.a = math.pi/2
        else:
            self.a = -1*math.pi/2

        agents = syudan
        #print(agents)

        num_hito = num_agents

        kabe = kabes

        num_kabe = num_kabes


        fa = self.syuui(num_hito,agents)

        #

        print("まえのself.a",self.a)

        self.a = kakudo_kai(fa, self.a)

        print("あとのself.a", self.a)

        #print("self.aは",self.a)
        kabe_f = self.kabe_f(num_kabe, kabe)

        hito_f = self.syuui_f(num_hito,agents)

        dvdt =( self.sokudo() + kabe_f + hito_f　)/2

        dvdt[0] = round(dvdt[0], 3) * math.cos(self.a)
        dvdt[1] = round(dvdt[1], 3) * math.sin(self.a)


        self.vi = self.vi + dvdt
        print("これは動く前のself.iti",self.iti)
        self.iti = self.iti + self.vi
        print("new_itiは",self.iti)



    def syuui(self, num, agents):

        #変数として
        mawari_hito = np.array([])
        for i in range(num):

            matome_i = self.iti - agents[i]
            #print("matome_i",matome_i,type(matome_i))

            hito_tan = (matome_i[0] / matome_i[1])
            kyori = ((matome_i[0])**2 + (matome_i[1])**2)**0.5
            #nij = matome_i / kyori
            if kyori <= self.dmax and agents[i,1] >= self.iti[i]:
                if (-1) * math.tan(self.a) <= hito_tan and hito_tan < + math.tan(self.a):
                    mawari_hito = np.append(mawari_hito, kyori)
        if mawari_hito.size == 0:
            fa = self.dmax
        else:
            fa = np.min(mawari_hito)
        return fa

    #def objective_function(theta, fa):
        return self.dmax * 2 + fa ** 2 - 2 * self.dmax * fa * math.cos(math.radians(self.a - theta))


    """
    def kakudo(self, fa):
            def objective_function(theta, fa):
                return self.dmax * 2 + fa ** 2 - 2 * self.dmax * fa * math.cos(math.radians(self.a - theta))

            min = optimize.fminbound(objective_function, -self.siyakaku, self.siyakaku)
            #これのminが次の角度aになる
            return min
    """
        #その後，ヒューリスティクスの第2段階を行う
        #それらの関数は以下に置いておく
    def kabe_f(self, num, kabe):
        kouryo = np.array([])
        for i in range(num):
            #print("@@@@@@@@@@",self.iti,kabe(i))
            matome_i = self.iti #- kabe(i)
            kabe_tan = (matome_i[0]/ matome_i[1])
            nagasa = ((matome_i[0])**2 + (matome_i[1])**2)**0.5
            niw = matome_i / nagasa
            if nagasa <= self.dmax :
                if (-1)*self.siyakaku <= kabe_tan and kabe_tan <+ self.siyakaku:
                    fiw = 0.5 * 9.8 * (self.m / 360 - nagasa)*(niw)
                    fiw = fiw / self.m
                    kouryo = np.append(kouryo, fiw)
        sum_fiw = np.sum(kouryo)
        return sum_fiw


    def syuui_f(self, num, agents):
        mawari_hito = np.array([])
        for i in range(num):
            matome_i = self.iti - agents[i]
            hito_tan = (matome_i[0]/ matome_i[1])
            kyori = ((matome_i[0])**2 + (matome_i[1])**2)**0.5
            nij = matome_i / kyori
            if kyori <= self.dmax :
                if (-1) * math.tan(self.siyakaku) <= hito_tan and hito_tan < + math.tan(self.siyakaku):
                    fij = 0.5 * 9.8 * ((self.m/360 * 2) - kyori) *(nij)
                    fij = fij / self.m
                    mawari_hito = np.append(mawari_hito, fij)
        sum_fij = np.sum(mawari_hito)
        return sum_fij

    def sokudo(self):
        dvdt = ((self.vdes-self.vi)/0.5)
               #+ self.kabe_f() +self.syuui_f()
        return dvdt



        #print(self.unique_id, self.kaisu, "目")



class Hokousya_ue(Agent):
    "人ですこれはmoussaidのヒューリスティクスにしたがう"

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        # これは設定されたパラメータ，一様である
        self.tyon = 0.5
        self.siyakaku = math.pi/4
        self.dmax = 10
        self.K = 5
        #self.a = (math.pi) / 2
        #self.vi = np.array([1.3,0])
        #self.vdes = np.array([1.3,0])*np.array([math.cos(self.a), math.sin(self.a)])
        # これは，歩行者エージェントごとに異なるもの，初期位置である
        coin = random.random()
        if coin < 0.3:
            self.iti_x = round(random.randrange(0, 10)*random.random(),3)
            self.iti_y = round(random.randrange(0, 5)*random.random(),3)
        else :
            self.iti_x = round(random.randrange(0, 10) * random.random(), 3)
            self.iti_y = round(random.randrange(40, 45, ) * random.random(), 3)
        if self.iti_y <= 10:
            self.a =  (math.pi) / 2
        else :
            self.a = -1*(math.pi)/2
        if self.iti_y <= 10:
            self.katikan = 1
        else:
            self.katikan = 0

        self.iti = np.array([self.iti_x, self.iti_y])
        self.vi = np.array([1.3, 0])
        self.vdes = np.array([1.3, 0]) * np.array([math.cos(self.a), math.sin(self.a)])
        self.mokutekiti_0 = np.array([self.iti_x, self.iti_y + 30 ])
        self.m = 60


    def step(self):

        "ここで関数を用いる"
        "まず，周囲の位置情報を確認する"
        #pass
        #周囲のエージェントとの距離の確認
        plt.scatter(self.iti[0], self.iti[1])

        if self.katikan == 1:
            self.a = math.pi/2
        else:
            self.a = -1*math.pi/2

        agents = syudan
        #print(agents)

        num_hito = num_agents

        kabe = kabes

        num_kabe = num_kabes


        fa = self.syuui(num_hito,agents)

        #

        print("まえのself.a",self.a)

        self.a = kakudo_kai(fa, self.a)

        print("あとのself.a", self.a)

        #print("self.aは",self.a)
        kabe_f = self.kabe_f(num_kabe, kabe)

        hito_f = self.syuui_f(num_hito,agents)

        dvdt = self.sokudo() + kabe_f + hito_f

        dvdt[0] = round(dvdt[0], 3) * math.cos(self.a)
        dvdt[1] = round(dvdt[1], 3) * math.sin(self.a)


        self.vi = self.vi + dvdt
        print("これは動く前のself.iti",self.iti)
        self.iti = self.iti + self.vi
        print("new_itiは",self.iti)



    def syuui(self, num, agents):

        #変数として
        mawari_hito = np.array([])
        for i in range(num):

            matome_i = self.iti - agents[i]
            #print("matome_i",matome_i,type(matome_i))

            hito_tan = (matome_i[0] / matome_i[1])
            kyori = ((matome_i[0])**2 + (matome_i[1])**2)**0.5
            #nij = matome_i / kyori
            if kyori <= self.dmax and agents[i,1] <= self.iti[1]:
                if (-1) * math.tan(self.a) <= hito_tan and hito_tan < + math.tan(self.a):
                    mawari_hito = np.append(mawari_hito, kyori)
        if mawari_hito.size == 0:
            fa = self.dmax
        else:
            fa = np.min(mawari_hito)
        return fa

    #def objective_function(theta, fa):
        return self.dmax * 2 + fa ** 2 - 2 * self.dmax * fa * math.cos(math.radians(self.a - theta))


    """
    def kakudo(self, fa):
            def objective_function(theta, fa):
                return self.dmax * 2 + fa ** 2 - 2 * self.dmax * fa * math.cos(math.radians(self.a - theta))

            min = optimize.fminbound(objective_function, -self.siyakaku, self.siyakaku)
            #これのminが次の角度aになる
            return min
    """
        #その後，ヒューリスティクスの第2段階を行う
        #それらの関数は以下に置いておく
    def kabe_f(self, num, kabe):
        kouryo = np.array([])
        for i in range(num):
            #print("@@@@@@@@@@",self.iti,kabe(i))
            matome_i = self.iti #- kabe(i)
            kabe_tan = (matome_i[0]/ matome_i[1])
            nagasa = ((matome_i[0])**2 + (matome_i[1])**2)**0.5
            niw = matome_i / nagasa
            if nagasa <= self.dmax :
                if (-1)*self.siyakaku <= kabe_tan and kabe_tan <+ self.siyakaku:
                    fiw = 0.5 * 9.8 * (self.m / 360 - nagasa)*(niw)
                    fiw = fiw / self.m
                    kouryo = np.append(kouryo, fiw)
        sum_fiw = np.sum(kouryo)
        return sum_fiw


    def syuui_f(self, num, agents):
        mawari_hito = np.array([])
        for i in range(num):
            matome_i = self.iti - agents[i]
            hito_tan = (matome_i[0]/ matome_i[1])
            kyori = ((matome_i[0])**2 + (matome_i[1])**2)**0.5
            nij = matome_i / kyori
            if kyori <= self.dmax :
                if (-1) * math.tan(self.siyakaku) <= hito_tan and hito_tan < + math.tan(self.siyakaku):
                    fij = 0.5 * 9.8 * ((self.m/360 * 2) - kyori) *(nij)
                    fij = fij / self.m
                    mawari_hito = np.append(mawari_hito, fij)
        sum_fij = np.sum(mawari_hito)
        return sum_fij

    def sokudo(self):
        dvdt = ((self.vdes-self.vi)/0.5)
               #+ self.kabe_f() +self.syuui_f()
        return dvdt



        #print(self.unique_id, self.kaisu, "目")

class Kabe(Agent):
    """横断歩道モデル"""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.iti = np.array([25,24])

    def step(self):
        pass


class Oundahodou(Model):
    """これはモデル　連続空間に配置する"""

    def __init__(self):
        self.num_agents = 10
        self.num_kabe = 1
        self.schedule = SimultaneousActivation(self)
        self.width = 10
        self.height = 50
        self.space = ContinuousSpace(self.width, self.height, True)
        self.syudan_hito = np.zeros((self.num_agents, 2))
        self.syudan_kabe = np.zeros((self.num_kabe, 2))
        self.time = 1000
        # Create agents
        for i in range(self.num_agents):
            a = Hokousya(i, self)
            self.schedule.add(a)
            self.syudan_hito[i,0] = a.iti_x
            self.syudan_hito[i,1] = a.iti_y
        #壁を作る
        for i in range(self.num_kabe):
            b = Kabe(i, self)
            self.schedule.add(b)
            self.syudan_kabe[i, 0] = b.iti[0]
            self.syudan_kabe[i, 1] = b.iti[1]




    def make_agents(self):
        """途中からアクティブになるエージェントの作成"""

    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()
        self.dasu_syudan_hito()
        self.fasu_num_agents()
        self.dasu_kabe()
        self.dasu_nu_kabe()

    def ptint_syudan(self):
        print(self.syudan)

    def dasu_syudan_hito(self):
        return self.syudan_hito

    def fasu_num_agents(self):
        return self.num_agents

    def dasu_kabe(self):
        return self.syudan_kabe

    def dasu_nu_kabe(self):
        return self.num_kabe


#syuudan_hito =prin




model = Oundahodou()
#print(model)

syudan = model.dasu_syudan_hito()
num_agents = model.num_agents
kabes = model.dasu_nu_kabe()
num_kabes = model.num_kabe
print("?------------------------",num_kabes,type(num_kabes))




for i in range(10):
    print(i,"ステップ目","&^&*(&^*(&^(*&^*&(^&(*^(&*%^&*(^&*(%^&*%&(*^%&^%(^")
    model.step()
    #plt.show()





