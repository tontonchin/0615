import numpy as np
from mesa import Agent, Model
import math
import random
from schedule import RandomActivationByBreed
import matplotlib.pyplot as plt
from hulistics_01 import kakudo, kakudo_kai,kakudo_kai_ue
from mesa.space import ContinuousSpace
import matplotlib.animation as animation

"""このプログラムは単なるテストである
タイムステップを増やすだけの単なるテストである"""
"""このプログラムを現在改修中"""

class Hokousya_sita(Agent):
    "人ですこれはmoussaidのヒューリスティクスにしたがう"

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        # これは設定されたパラメータ，一様である
        self.tyon = 0.5
        self.siyakaku = math.pi/2
        self.dmax = 5
        self.K = 5
        self.vi = 1.3
        # これは，歩行者エージェントごとに異なるもの，初期位置である


        self.iti_x = round(random.randrange(0, 5)+random.random(),2)
        self.iti_y = round(random.randrange(0, 5)+random.random(),2)


        self.a =  (math.pi) / 2

        self.iti = np.array([self.iti_x, self.iti_y])
        self.vi = np.array([0, 1.3])
        self.vdes = np.array([0, 1.3])
        self.m = 60
        self.a = math.pi/2
        self.theta = 0
        self.tan_siya = math.tan(self.siyakaku)


    def step(self):

        "imという関数について，1座標を追加"
        im_x_sita.append(self.iti[0])
        im_y_sita.append(self.iti[1])

        #1ステップごとに価値観を変更，目的方向は垂直に上
        self.a = math.pi/2
        agents = syudan

        num_hito = num_agents

        kabe = kabes

        num_kabe = num_kabes


        fa, syu_num , syuui_agents= self.syuui(num_hito,agents)


        self.a = kakudo_kai(fa, self.a)

        self.vdes = 1.3
        self.vdes = self.vdes * np.array([math.cos(self.a), math.sin(self.a)])


        print("Unique_ID", self.unique_id)
        hito_f = self.syuui_f(syu_num,syuui_agents)

        print("syu_agents",syuui_agents)

        V_nomi = self.sokudo()
        dvdt = (V_nomi + hito_f + self.douro_f() ) /100
        print("self.douro_f()",self.douro_f())
        print("hito_f",hito_f)

        dvdt_new = dvdt

        print("dvdt_new", dvdt_new)

        print("self.vdes",self.vdes)
        print("これは動く前のself.vi", self.vi)
        maeno_vi = self.vi
        self.vi = self.vi + dvdt_new

        dvdt[0] = round(dvdt[0], 3)
        dvdt[1] = round(dvdt[1], 3)

        tan_theta = math.tan(self.a)

        #if dvdt[1] <= 0 :
         #   dvdt[1] = 0
        #else:
         #54   tan_theta = dvdt[0]/dvdt[1]

        if round(dvdt[0], 2) != 0:
            print("横方向に動いた!!!!!!!!!!")

        tan_the_p_siya = (tan_theta + math.tan(self.siyakaku))/ (1 - (tan_theta * math.tan(self.siyakaku)))

        if tan_the_p_siya <= 0 :
            tan_the_p_siya = (-1)* tan_the_p_siya

        self.tan_siya = tan_the_p_siya


        for i in range(num_agents):
            if self.iti[0]==syudan[i,0] and self.iti[1]==syudan[i,1]:
                syudan[i] += self.vi
        #print("これはdtdsv", dvdt)
        print("これは辺が後のself.vi",self.vi)
        print("これは動く前のself.iti",self.iti)
        self.iti = self.iti + self.vi
        print("new_itiは",self.iti)

        if np.linalg.norm(self.vi) - np.linalg.norm(maeno_vi) >= 0.8:
            print("これは予測できない変化が発生しました")
            #print("これは辺が前のself.vi",maeno_vi)
            #print("これは辺が後のself.vi",self.vi)
            print("v_nomi",V_nomi)



    def syuui(self, num, agents):

        #変数として
        mawari_hito = np.array([])
        mawari_syudan_kakudo = np.array([0, 0])
        syuui_agents = np.array([0,0])
        for i in range(num):

            matome_i =  agents[i] - self.iti
            #print("matome_i",matome_i,type(matome_i))

            hito_tan = (matome_i[1] / matome_i[0])
            #kyori = ((matome_i[0])**2 + (matome_i[1])**2)**0.5
            kyori =np.linalg.norm(matome_i)
            #hito_sin = matome_i[1]/kyori
            #hito_cos = matome_i[0]/kyori
            if kyori <= self.dmax and agents[i,1] >= self.iti[1]:
                #if (-1) * self.tan_siya <= hito_tan and hito_tan <= self.tan_siya:
                if hito_tan >= 0:
                    if hito_tan >= self.tan_siya:
                        mawari_hito = np.append(mawari_hito, kyori)
                        syuui_agents = np.vstack(([syuui_agents, agents[i]]))
                else:
                    if hito_tan <= self.tan_siya:
                        mawari_hito = np.append(mawari_hito, kyori)
                        syuui_agents = np.vstack(([syuui_agents, agents[i]]))

        if mawari_hito.size == 0:
            fa = self.dmax
        else:
            fa = np.min(mawari_hito)
        #mawari_syudan_kakudo = np.delete(mawari_syudan_kakudo, 0, axis=0)
        syuui_agents = np.delete(syuui_agents, 0, axis=0)

        return fa,mawari_hito.size,syuui_agents

    #def objective_function(theta, fa):
        #return self.dmax * 2 + fa ** 2 - 2 * self.dmax * fa * math.cos(math.radians(self.a - theta))


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
            matome_i = kabe[i] - self.iti
            kabe_tan = (matome_i[1]/ matome_i[0])
            #nagasa = ((matome_i[0])**2 + (matome_i[1])**2)**0.5
            nagasa = np.linalg.norm(matome_i)
            niw = matome_i / nagasa
            if nagasa <= self.dmax and kabe[i,1] >= self.iti[1] :
                if (-1) * math.tan(self.siyakaku) <= kabe_tan and kabe_tan < + math.tan(self.siyakaku):
                    fiw = 0.5 * 9.8 * (self.m / 220 - nagasa)*(niw)
                    fiw = fiw / self.m
                    kouryo = np.append(kouryo, fiw)
        sum_fiw = np.sum(kouryo)
        kabe_f = sum_fiw
        return sum_fiw

    def douro_f(self):
        fiw = 0
        fiw = 0.005 *(9.8 * (60 / 100 - self.iti[0]) - 9.8 * (60 / 100 - abs(10 - self.iti[0])))
        fiw = 0
        fiw_douro = np.array([fiw, 0])
        return fiw_douro

    def syuui_f(self, num, agents ):
        mawari_hito = np.array([0,0])
        for i in range(num):
            # 位置関係
            matome_i = agents[i] - self.iti
            hito_tan = (matome_i[1] / matome_i[0])
            # kyori = ((matome_i[0])**2 + (matome_i[1])**2)**0.5
            kyori = np.linalg.norm(matome_i)
            nij = -1*(matome_i / kyori)
            print("nij",nij,type(nij))

            tan_matome = (math.tan(self.siyakaku)+math.tan(self.a))/(1 - (math.tan(self.siyakaku)*math.tan(self.a)))

            if kyori <= self.dmax and agents[i, 1] >= self.iti[1]:
                #if (-1) * math.tan(self.siyakaku) <= hito_tan and hito_tan < + math.tan(self.siyakaku):
                #if (-1) * tan_matome <= hito_tan and hito_tan <= tan_matome:
                if tan_matome >= 0:
                    if tan_matome >= self.tan_siya:
                        fij = 0.25 * 9.8 * ((self.m /60 * 2) - kyori) * (nij)
                        fij = fij / self.m
                        print("fij", fij)
                        f_ij = np.array([fij[0],fij[1]])
                        mawari_hito = mawari_hito + f_ij
                else:
                    if tan_matome <= self.tan_siya:
                        fij = 0.25 * 9.8 * ((self.m / 60 * 2) - kyori) * (nij)
                        fij = fij / self.m
                        print("fij", fij)
                        f_ij = np.array([fij[0], fij[1]])
                        mawari_hito = mawari_hito + f_ij

        #sum_fij = np.sum(mawari_hito,axis=0)
        print("sum_fij", mawari_hito)
        #syuui_f = np.array([math.cos(self.a) * sum_fij, math.sin(self.a) * sum_fij])
        return mawari_hito

    def sokudo(self):
        dvdt = ((self.vdes - self.vi) / 0.5)
            # + self.kabe_f() +self.syuui_f()
        return dvdt


        #print(self.unique_id, self.kaisu, "目")




class Hokousya_ue(Agent):
    "人ですこれはmoussaidのヒューリスティクスにしたがう"

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        # これは設定されたパラメータ，一様である
        self.tyon = 0.5
        self.siyakaku = math.pi/2
        self.dmax = 5
        self.K = 5
        #self.a = (math.pi) / 2
        #self.vi = np.array([1.3,0])
        #self.vdes = np.array([1.3,0])*np.array([math.cos(self.a), math.sin(self.a)])
        # これは，歩行者エージェントごとに異なるもの，初期位置である


        self.iti_x = round(random.randrange(0, 5)+random.random(),2)
        self.iti_y = round(random.randrange(45, 50)+random.random(),2)


        self.a =  3* (math.pi) / 2

        self.iti = np.array([self.iti_x, self.iti_y])
        self.vi = np.array([0, -1.3])
        self.vdes = np.array([0, -1.3])
        self.m = 60
        self.tan_siya = math.tan(self.siyakaku)


    def step(self):

        "ここで関数を用いる"
        "まず，周囲の位置情報を確認する"
        #pass
        #周囲のエージェントとの距離の確認
        #im.append(plt.scatter(self.iti[0], self.iti[1]))

        #plt.scatter(self.iti[0], self.iti[1])

        self.vdes = 1.3

        im_x_ue.append(self.iti[0])
        im_y_ue.append(self.iti[1])

        self.a = 3*(math.pi/2)

        agents = syudan
        #print(agents)

        num_hito = num_agents

        kabe = kabes

        num_kabe = num_kabes


        fa, syu_num,agents = self.syuui(num_hito,agents)

        print("上からsyu_agents", agents)



        #print("まえのself.a",self.a)

        maeno_a = self.a

        self.a = kakudo_kai_ue(fa, self.a)

        print("へんかあとのかくどは!!!!!!!!",math.degrees(self.a))
        if maeno_a != self.a:
            print("変化しました角度変化しました角度")

        self.vdes = self.vdes * np.array([math.cos(self.a), math.sin(self.a)])


        print("Unique_ID", self.unique_id)
        hito_f = self.syuui_f(syu_num,agents)

        #2で割ったことにより1ステップごとのdvdtは0.5秒となる

        V_nomi = self.sokudo()
        dvdt = (V_nomi + hito_f + self.douro_f() ) / 100


        print("self.douro_f()",self.douro_f())
        print("hito_f",hito_f)



        #dvdt[0] = round(dvdt[0], 3)
        #dvdt[1] = round(dvdt[1], 3)

        #if dvdt[1] >= 0 :
            #dvdt[1] = 0



        #print("dvdt_matome", dvdt_matome)

        dvdt_new = dvdt

        print("dvdt_new", dvdt_new)


        print("self.vdes",self.vdes)
        print("これは動く前のself.vi", self.vi)
        maeno_vi = self.vi
        self.vi = self.vi + dvdt_new



        dvdt[0] = round(dvdt[0], 3)
        dvdt[1] = round(dvdt[1], 3)

        tan_theta = math.tan(self.a)
        if dvdt[1] >= 0 :
            dvdt[1] = 0
        else:
            tan_theta = dvdt[0]/dvdt[1]

        tan_the_p_siya = (tan_theta + math.tan(self.siyakaku))/ (1 - (tan_theta * math.tan(self.siyakaku)))

        if tan_the_p_siya <= 0 :
            tan_the_p_siya = (-1)* tan_the_p_siya

        self.tan_siya = tan_the_p_siya



        for i in range(num_agents):
            if self.iti[0]==syudan[i,0] and self.iti[1]==syudan[i,1]:
                syudan[i] += self.vi
        #print("これはdtdsv", dvdt)
        print("これは辺が後のself.vi",self.vi)
        print("これは動く前のself.iti",self.iti)
        self.iti = self.iti + self.vi
        print("new_itiは",self.iti)

        if np.linalg.norm(self.vi) - np.linalg.norm(maeno_vi) >= 0.8:
            print("これは予測できない変化が発生しました")
            #print("これは辺が前のself.vi",maeno_vi)
            #print("これは辺が後のself.vi",self.vi)
            print("v_nomi",V_nomi)



    def syuui(self, num, agents):

        #変数として
        mawari_hito = np.array([])
        syuui_agents = np.array([0, 0])
        for i in range(num):

            matome_i =  agents[i] - self.iti
            #print("matome_i",matome_i,type(matome_i))

            hito_tan = (matome_i[1] / matome_i[0])
            #kyori = ((matome_i[0])**2 + (matome_i[1])**2)**0.5
            kyori =np.linalg.norm(matome_i)
            if kyori <= self.dmax and agents[i,1] >= self.iti[1]:
                #if (-1) * self.tan_siya <= hito_tan and hito_tan <= self.tan_siya:
                if hito_tan >= 0:
                    if hito_tan >= self.tan_siya:
                        mawari_hito = np.append(mawari_hito, kyori)
                        syuui_agents = np.vstack(([syuui_agents, agents[i]]))
                else:
                    if hito_tan <= self.tan_siya:
                        mawari_hito = np.append(mawari_hito, kyori)
                        syuui_agents = np.vstack(([syuui_agents, agents[i]]))

                    #mawari_hito = np.append(mawari_hito, kyori)
                    #syuui_agents = np.vstack(([syuui_agents, agents[i]]))
        if mawari_hito.size == 0:
            fa = self.dmax
        else:
            fa = np.min(mawari_hito)
        syuui_agents = np.delete(syuui_agents, 0, axis=0)
        return fa,mawari_hito.size,syuui_agents

    #def objective_function(theta, fa):
        #return self.dmax * 2 + fa ** 2 - 2 * self.dmax * fa * math.cos(math.radians(self.a - theta))


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
            matome_i = kabe[i] - self.iti
            kabe_tan = (matome_i[1]/ matome_i[0])
            #nagasa = ((matome_i[0])**2 + (matome_i[1])**2)**0.5
            nagasa = np.linalg.norm(matome_i)
            niw = matome_i / nagasa
            if nagasa <= self.dmax and kabe[i,1] >= self.iti[1] :
                if math.tan(self.siyakaku + (3 * math.pi / 2)) <= kabe_tan and kabe_tan < + math.tan((3 * math.pi / 2) - self.siyakaku):
                    fiw = 0.5 * 9.8 * (self.m / 100 - nagasa)*(niw)
                    fiw = fiw / self.m
                    kouryo = np.append(kouryo, fiw)
        sum_fiw = np.sum(kouryo)
        print("sum_fiw",sum_fiw)
        return sum_fiw

    def douro_f(self):

        fiw = 0.005 * (9.8 * (60/220 - self.iti[0]) - 9.8 * (60/220 - abs(10 - self.iti[0])))
        fiw = 0
        fiw_douro = np.array([fiw, 0])
        return fiw_douro




    def syuui_f(self, num, agents):
        mawari_hito = np.array([0,0])
        for i in range(num):
            #位置関係
            matome_i = agents[i] - self.iti
            print("matome_i",matome_i)
            hito_tan = (matome_i[1]/ matome_i[0])
            #kyori = ((matome_i[0])**2 + (matome_i[1])**2)**0.5
            kyori = np.linalg.norm(matome_i)
            nij = (-1)*(matome_i / kyori)
            tan_matome = (math.tan(self.siyakaku) + math.tan(self.a)) / (
                        1 - (math.tan(self.siyakaku) * math.tan(self.a)))

            if kyori <= self.dmax and agents[i, 1] >= self.iti[1]:
                if tan_matome >= 0:
                    if tan_matome >= self.tan_siya:
                        fij = 0.25 * 9.8 * ((self.m / 60 * 2) - kyori) * (nij)
                        fij = fij / self.m
                        f_ij = np.array([fij[0], fij[1]])
                        mawari_hito = mawari_hito + f_ij
                else:
                    if tan_matome <= self.tan_siya:
                        fij = 0.25 * 9.8 * ((self.m / 60 * 2) - kyori) * (nij)
                        fij = fij / self.m
                        f_ij = np.array([fij[0], fij[1]])
                        mawari_hito = mawari_hito + f_ij
        #sum_fij = np.sum(mawari_hito, axis=0)
        print("sum_fij", mawari_hito)
        #syuui_f = np.array([math.cos(self.a)*sum_fij, math.sin(self.a)*sum_fij])
        return mawari_hito

    def sokudo(self):
        dvdt = ((self.vdes-self.vi)/0.5)
               #+ self.kabe_f() +self.syuui_f()
        return dvdt



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
        self.num_agents_sita = 30
        self.num_agents_ue = 30
        self.num_kabe = 1
        self.schedule = RandomActivationByBreed(self)
        #self.schedule = RandomActivation(self)
        self.width = 10
        self.height = 50
        self.space = ContinuousSpace(self.width, self.height, True)
        self.syudan_hito_sita = np.zeros((self.num_agents_sita, 2))
        self.syudan_hito_ue = np.zeros((self.num_agents_ue, 2))
        self.syudan_kabe = np.zeros((self.num_kabe, 2))
        self.time = 1000
        # Create agents

        for j in range(self.num_agents_sita):
            a = Hokousya_sita(j, self)
            self.syudan_hito_sita[j,0] = a.iti_x
            self.syudan_hito_sita[j,1] = a.iti_y
            self.schedule.add(a)
            #self.syudan_hito_sita[i,0] = a.iti_x
            #self.syudan_hito_sita[i,1] = a.iti_y

        for i in range(self.num_agents_ue):
            b = Hokousya_ue(i, self)
            self.syudan_hito_ue[i, 0] = b.iti_x
            self.syudan_hito_ue[i, 1] = b.iti_y
            self.schedule.add(b)
            #self.syudan_hito_ue[i,0] = b.iti_x
            #self.syudan_hito_ue[i,1] = b.iti_y

        #壁を作る
        for i in range(self.num_kabe):
            c = Kabe(i, self)
            self.schedule.add(c)
            self.syudan_kabe[i, 0] = c.iti[0]
            self.syudan_kabe[i, 1] = c.iti[1]




    def make_agents(self):
        """途中からアクティブになるエージェントの作成"""
        for j in range(self.num_agents_sita):
            d = Hokousya_sita(j, self)
            self.syudan_hito_sita[j,0] = d.iti_x
            self.syudan_hito_sita[j,1] = d.iti_y
            self.schedule.add(d)
            #self.syudan_hito_sita[i,0] = a.iti_x
            #self.syudan_hito_sita[i,1] = a.iti_y

        for i in range(self.num_agents_ue):
            e = Hokousya_ue(i, self)
            self.syudan_hito_ue[i, 0] = e.iti_x
            self.syudan_hito_ue[i, 1] = e.iti_y
            self.schedule.add(e)
            #self.syudan_hito_ue[i,0] = b.iti_x
            #self.syudan_hito_ue[i,1] = b.iti_y

    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()
        self.dasu_syudan_hito()
        self.fasu_num_agents()
        self.dasu_kabe()
        self.dasu_nu_kabe()

    """モデル描画を目指す"""
    #def make_im(self):
        #for i in range(self.num_agents):
            #im = ax.plot()

    def ptint_syudan(self):
        print(self.syudan)

    def dasu_syudan_hito(self):
        self.syudan_hito = np.append(self.syudan_hito_sita,self.syudan_hito_ue,axis=0)
        return self.syudan_hito

    def fasu_num_agents(self):
        return self.num_agents_sita + self.num_agents_ue

    def dasu_kabe(self):
        return self.syudan_kabe

    def dasu_nu_kabe(self):
        return self.num_kabe


#syuudan_hito =prin

#位置座標についての設定




model = Oundahodou()
#print(model)

syudan = model.dasu_syudan_hito()
print("エージェントの集団です",syudan)
num_agents = model.num_agents_ue + model.num_agents_sita
print("num_agent",num_agents)
kabes = model.dasu_nu_kabe()
num_kabes = model.num_kabe
print("?------------------------",num_kabes,type(num_kabes))




fig = plt.figure()
ims = []

im_x_ue = []
im_y_ue = []

im_x_sita = []
im_y_sita = []

for i in range(30):
    im_x_ue = []
    im_y_ue = []

    im_x_sita = []
    im_y_sita = []
    #im_scatter = plt.scatter(im_x, im_y)
    #ims.append(im_scatter)
    print(i,"ステップ目","&^&*(&^*(&^(*&^*&(^&(*^(&*%^&*(^&*(%^&*%&(*^%&^%(^")
    model.step()
    #plt.xlim(0, 10)
    #plt.ylim(-10, 70)
    #plt.title("time = "+str(i))
    im_scatter_ue = plt.scatter(im_x_ue, im_y_ue,c="blue")
    im_scatter_sita = plt.scatter(im_x_sita, im_y_sita, c="red")
    ims.append([im_scatter_ue, im_scatter_sita])
    print(i,"ステップ目","syudan",syudan)
    #if i == 5 :
        #model.make_agents()


   #散布図
    # アニメーション作成

#print(ims)

anim = animation.ArtistAnimation(fig, ims,interval=500)
anim.save('kotu_0114_asita_anim.gif', writer='writer', fps=4)


plt.show()



