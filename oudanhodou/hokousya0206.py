import numpy as np
from mesa import Agent, Model
import math
import random
from schedule import RandomActivationByBreed
import matplotlib.pyplot as plt
from hulistics_01 import kakudo, kakudo_kai,kakudo_kai_ue, kakudo_kai_sita
from mesa.space import ContinuousSpace
import matplotlib.animation as animation

"""このプログラムは単なるテストである
タイムステップを増やすだけの単なるテストである"""
"""このプログラムを現在改修中"""
"""第一のヒューリスティクスのβガンまを考慮にいれたもの，下の作成"""

class Hokousya_sita(Agent):
    "人ですこれはmoussaidのヒューリスティクスにしたがう"

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        # これは設定されたパラメータ，一様である
        self.tyon = 0.5
        self.siyakaku = math.pi/2
        self.dmax = 10
        self.K = 5
        self.vi = 1.3
        # これは，歩行者エージェントごとに異なるもの，初期位置である


        self.iti_x = round(random.randrange(0, 20)+random.random(),3)
        #self.iti_x = 5
        self.iti_y = round(random.randrange(0, 25)+random.random(),3)
        #self.iti_y = 10


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
        #self.a = math.radians(random.randrange(1,180))

        agents = syudan
        print("agents", agents)
        num_hito = num_agents
        kabe = kabes
        num_kabe = num_kabes

        kabe_hani = kabe_han

        fa , fa_zahyou = self.dasu_fa_kai(num_hito,agents)

        if fa_zahyou[0] >= 1:
            print("これがみたかった　")


        print("fa_zahyou_type",type(fa_zahyou))



        fa_kyori = np.linalg.norm(fa_zahyou)

        beta = math.acos(fa_zahyou[0]/(fa_kyori+60/220))

        ganma = math.acos(fa_zahyou[0]/(fa_kyori-60/220))

        maeno_a = self.a

        self.a = kakudo_kai_sita(fa, self.a, beta, ganma)
        if fa < self.dmax and self.a != maeno_a:
            print("第一のあれにつかうfa",fa,math.degrees(self.a),"前の角度は",math.degrees(maeno_a))
            if not fa_zahyou[0] == 0 and fa_zahyou[1] == 0:
                print("fa_zahyouうんこ",fa_zahyou)

        #vdesについての流れ
        self.vdes = 1.3
        vdes_kouho = fa / 0.5
        if vdes_kouho <= self.vdes:
            self.vdes = vdes_kouho
        self.vdes = self.vdes * np.array([math.cos(self.a), math.sin(self.a)])


        print("Unique_ID", self.unique_id)


        #hito_f = self.syuui_f(num_hito,agents)
        hito_f = 0
        print(hito_f)

        V_nomi = self.sokudo()
        douro_f = self.douro_f()
        dvdt = (V_nomi + hito_f + douro_f ) /10
        print("self.douro_f()",self.douro_f())
        print("hito_f",hito_f)

        dvdt[0] = round(dvdt[0], 3)
        dvdt[1] = round(dvdt[1], 3)


        maeno_vi = self.vi
        self.vi = self.vi + dvdt

        for i in range(num_agents):
            if self.iti[0]==syudan[i,0] and self.iti[1]==syudan[i,1]:
                syudan[i] += (self.vi)
        #print("これはdtdsv", dvdt)
        print("これは辺が後のself.vi",self.vi)
        print("これは動く前のself.iti",self.iti)
        self.iti = self.iti + self.vi
        print("new_itiは",self.iti)

        if np.linalg.norm(self.vi) - np.linalg.norm(maeno_vi) >= 0.8:
            print("これは予測できない変化が発生しました")
            print("v_nomi",V_nomi)



    def dasu_fa(self, num, agents):
        #この関数はテストすんだ＼
        matome = agents - self.iti
        fa_kouho = np.array([10])
        for i in range(num):
            if matome[i,0] == 0  and matome[i,1]==0:
                continue
            alpha_wasi_omae = math.atan(matome[i][1] / matome[i][0])
            kakudosa = abs(alpha_wasi_omae - self.a)
            if kakudosa <= 0.04:
                kyori = np.linalg.norm(matome[i])
                if kyori <= self.dmax:
                    fa_kouho = np.append(fa_kouho, kyori)
                    print("matome_iのあれ",matome[i])
        if fa_kouho.size == 0:
            fa = self.dmax
        else:
            fa = np.min(fa_kouho)
        print("これがfa",fa)
        return fa


    def dasu_fa_kai(self, num, agents):
        #この関数はテストすんだ＼
        matome = agents - self.iti
        fa_kouho = np.array([10])
        fa_zahyou = np.array([[0,0]])
        for i in range(num):
            if matome[i,0] == 0  and matome[i,1]==0:
                print("地震の座標は",)
                continue
            kyori = np.linalg.norm(matome[i])
            alpha_wasi_omae = math.acos(matome[i][0] / kyori)
            kakudosa = abs(alpha_wasi_omae - self.a)
            if kakudosa <= 0.04 and matome[i,1] >= 0:
                #kyori = np.linalg.norm(matome[i])
                if kyori <= self.dmax:
                    fa_kouho = np.append(fa_kouho, kyori)
                    fa_zahyou = np.append(fa_zahyou,[[matome[i][0],matome[i][1]]],axis=0)
                    print("matome_iのあれ", matome[i])
        if fa_kouho.size == 1:
            fa = self.dmax
            fa_zahyou_tada = np.array([0,0])
        else:
            fa = np.min(fa_kouho)
            fa_n = np.argmin(fa_kouho)
            print("fa_n", fa_n)
            print("fa_zahyou",fa_zahyou)
            fa_zahyou_tada = np.array([fa_zahyou[fa_n,0],fa_zahyou[fa_n,1]])

        fa_zahyou_tada[0] = round(fa_zahyou_tada[0], 3)
        fa_zahyou_tada[1] = round(fa_zahyou_tada[1], 3)

        print("おーいお茶",fa_zahyou_tada)

        print("これがfa",fa)
        return fa , fa_zahyou_tada



    def kabe_fa(self,hito_fa, kabe, kabe_iti):
        fa_naka = 10
        if hito_fa <= self.dmax:
            fa_naka = hito_fa
        fa_kouho = np.array([fa_naka])
        for xi in kabe_iti:
            if abs(xi -self.iti[0]) <= 0.1:
                y_ = - ((kabe[0] * xi) + kabe[2]) / (kabe[1])
                kyori = y_ - self.iti[1]
                fa_kouho = np.append(fa_kouho, kyori)
        uv = np.amin(fa_kouho)
        return uv


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

        if abs(self.iti[0]) <= 60 / 220:
            a = abs(self.iti[0])
            fiw = 3 * (a * (60 / 220 - self.iti[0]) - 9.8 * (60 / 220 - abs(10 - self.iti[0])))

        elif abs(20-self.iti[0])<= 60/220:
            b = abs(20 - self.iti[0])
            fiw = 3  * (b * (60 / 220 - self.iti[0]) - 9.8 * (60 / 220 - abs(10 - self.iti[0])))
        fiw_douro = np.array([fiw, 0])
        fiw_douro = np.array([0, 0])
        return fiw_douro

    def syuui_f(self, num, agents ):
        mawari_hito = np.array([0,0])
        for i in range(num):
            # 位置関係
            if abs(self.iti[0] - agents[i][0]) <= 0.6 and abs(self.iti[1] - agents[i][1]) <= 0.6:
                matome_i = agents[i] - self.iti
                if matome_i[0] == 0:
                    if self.a >= 0 and self.a <= math.pi:
                        kakudo = (math.pi/2)
                    elif self.a > math.pi and self.a <= 2 * math.pi:
                        kakudo = 3 * (math.pi/2)
                else:
                    kakudo = math.atan(matome_i[1]/ matome_i[0])
                nij = -1*(np.array([math.sin(kakudo), math.cos(kakudo)]))
                kyori = np.linalg.norm(matome_i)
                fij = 5000 * kyori * ((self.m /220 * 2) - kyori) * (nij)
                fij = fij / self.m
                fij[0] = round(fij[0] , 4)
                fij[1] = round(fij[1], 4)

                print("fij", fij)
                f_ij = np.array([fij[0],fij[1]])
                mawari_hito = mawari_hito + f_ij
        print("sum_fij", mawari_hito)
        return mawari_hito

    def syuui_f_1(self, num, agents ):
        mawari_hito = np.array([0,0])
        for i in range(num):
            # 位置関係
            matome_i = agents[i] - self.iti
            kyori = np.linalg.norm(matome_i)
            nij = np.array([0,0])
            try:
                nij = -1*(matome_i / kyori)
            except RuntimeWarning:
                nij = (math.sin(math.pi/2), math.cos(math.pi/2))
            print("nij",nij,type(nij))

            tan_matome = (math.tan(self.siyakaku)+math.tan(self.a))/(1 - (math.tan(self.siyakaku)*math.tan(self.a)))

            if abs(self.iti[0] - agents[i][0]) <= 0.5 and abs(self.iti[1] - agents[i][1]) <= 0.5:
                fij = -5000 * kyori * ((self.m /220 * 2) - kyori) * (nij)
                fij = fij / self.m
                print("fij", fij)
                f_ij = np.array([fij[0],fij[1]])
                mawari_hito = mawari_hito + f_ij
        return mawari_hito

    def sokudo(self):
        dvdt = ((self.vdes - self.vi) / 0.5)
            # + self.kabe_f() +self.syuui_f()
        return dvdt



class Hokousya_ue(Agent):
    "人ですこれはmoussaidのヒューリスティクスにしたがう"

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        # これは設定されたパラメータ，一様である
        self.tyon = 0.5
        self.siyakaku = math.pi/2
        self.dmax = 10
        self.K = 10
        self.iti_x = round(random.randrange(0, 20)+random.random(),3)
        #self.iti_x = 5
        self.iti_y = round(random.randrange(26, 50)+random.random(),3)
        #self.iti_y = 10
        self.a =  3* (math.pi) / 2
        self.iti = np.array([self.iti_x, self.iti_y])
        self.vi = np.array([0, -1.3])
        self.vdes = np.array([0, -1.3])
        self.m = 60
        self.tan_siya = math.tan(self.siyakaku)


    def step(self):
        im_x_ue.append(self.iti[0])
        im_y_ue.append(self.iti[1])

        self.a = 3*(math.pi/2)
        agents = syudan
        num_hito = num_agents
        kabe = kabes
        num_kabe = num_kabes


        fa = self.dasu_fa(num_hito,agents)
        maeno_a = self.a

        self.a = kakudo_kai_ue(fa, self.a)
        if fa != self.dmax:
            print("第一のあれにつかうfa",fa,self.a)
            print("第一のあれにつかうfa",fa,self.a)

        if maeno_a != self.a:
            print("第一のヒューリスティクスにより角度変化",maeno_a, math.degrees(self.a))

        self.vdes = 1.3
        vdes_kouho = fa / 0.5
        if vdes_kouho <= self.vdes:
            self.vdes = vdes_kouho
        self.vdes = self.vdes * np.array([math.cos(self.a), math.sin(self.a)])


        print("Unique_ID", self.unique_id)
        hito_f = self.syuui_f(num_hito,agents)

        if hito_f[0] != 0 or hito_f[1]!= 0:
            print("人の接触力が起こった",hito_f)
        V_nomi = self.sokudo()
        douro_f = self.douro_f()
        dvdt = (V_nomi + hito_f + douro_f ) / 10
        print("self.douro_f()",self.douro_f())
        print("hito_f",hito_f)

        dvdt[0] = round(dvdt[0], 3)
        dvdt[1] = round(dvdt[1], 3)
        print("dvdt_new", dvdt)
        print("self.vdes",self.vdes)
        print("これは動く前のself.vi", self.vi)
        maeno_vi = self.vi
        self.vi = self.vi + dvdt

        for i in range(num_agents):
            if self.iti[0]==syudan[i,0] and self.iti[1]==syudan[i,1]:
                syudan[i] += (self.vi)
        #print("これはdtdsv", dvdt)
        print("これは辺が後のself.vi",self.vi)
        print("これは動く前のself.iti",self.iti)
        self.iti = self.iti + self.vi
        print("new_itiは",self.iti)

        if np.linalg.norm(self.vi) - np.linalg.norm(maeno_vi) >= 0.8:
            print("これは予測できない変化が発生しました")
            print("v_nomi",V_nomi)

    def dasu_fa(self, num, agents):
        matome = agents - self.iti
        fa_kouho = np.array([10])
        for i in range(num):
            if matome[i][0] == 0  and matome[i][1]==0:
                continue
            alpha_wasi_omae = math.atan(matome[i][1] / matome[i][0])
            kakudosa = abs(alpha_wasi_omae - self.a)
            if kakudosa <= 0.04:
                kyori = np.linalg.norm(matome[i])
                if kyori <= self.dmax:
                    fa_kouho = np.append(fa_kouho, kyori)
        if fa_kouho.size == 0:
            fa = self.dmax
        else:
            fa = np.min(fa_kouho)
        return fa

    def kabe_fa(self,hito_fa, kabe, kabe_iti):
        if hito_fa <= self.dmax:
            fa = hito_fa
        fa_kouho = np.array([fa])
        for xi in kabe_iti:
            if abs(xi -self.iti[0]) <= 0.1:
                y_ = - ((kabe[0] * xi) + kabe[2]) / (kabe[1])
                kyori = y_ - self.iti[1]
                fa_kouho = np.append(fa_kouho, kyori)
        fa = np.amin(fa_kouho)
        return -fa

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
                    fiw = 1 * 9.8 * (self.m / 100 - nagasa)*(niw)
                    fiw = fiw / self.m
                    kouryo = np.append(kouryo, fiw)
        sum_fiw = np.sum(kouryo)
        return sum_fiw

    def douro_f(self):

        fiw = 0

        if abs(self.iti[0]) <= 60 / 220:
            a = abs(self.iti[0])
            fiw = 3 * (a * (60 / 220 - self.iti[0]) - 9.8 * (60 / 220 - abs(10 - self.iti[0])))

        elif abs(20-self.iti[0])<= 60/220:
            b = abs(20-self.iti[0])
            fiw = 3 * (b * (60 / 220 - self.iti[0]) - 9.8 * (60 / 220 - abs(10 - self.iti[0])))
        fiw_douro = np.array([fiw, 0])
        fiw_douro = np.array([0, 0])


        return fiw_douro


    def syuui_f(self, num, agents ):
        mawari_hito = np.array([0,0])
        for i in range(num):
            # 位置関係
            if abs(self.iti[0] - agents[i][0]) <= 0.6 and abs(self.iti[1] - agents[i][1]) <= 0.6:
                matome_i = agents[i] - self.iti
                if matome_i[0] == 0:
                    if self.a >= 0 and self.a <= math.pi:
                        kakudo = (math.pi/2)
                    elif self.a > math.pi and self.a <= 2 * math.pi:
                        kakudo = (3*math.pi/2)
                else:
                    kakudo = math.atan(matome_i[1]/ matome_i[0])
                print("kakudo", kakudo)
                nij = np.array([math.sin(kakudo), math.cos(kakudo)])
                kyori = np.linalg.norm(matome_i)
                fij = -5000 * kyori * ((self.m /220 * 2) - kyori) * (nij)
                fij = fij / self.m
                fij[0] = round(fij[0], 4)
                fij[1] = round(fij[1], 4)


                print("fij", fij, type(fij))
                f_ij = np.array([fij[0],fij[1]])
                mawari_hito = mawari_hito + f_ij
        print("sum_fij", mawari_hito)
        return mawari_hito


    def sokudo(self):
        dvdt = ((self.vdes-self.vi)/0.5)
               #+ self.kabe_f() +self.syuui_f()
        return dvdt



class Kabe(Agent):
    """横断歩道モデル"""

    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.naka = np.array([1,-1,10])
        self.kabe_iti = np.arange(0,2,0.1)



    def step(self):
        pass




class Oundahodou(Model):
    """これはモデル　連続空間に配置する"""

    def __init__(self):
        self.num_agents_sita = 5
        self.num_agents_ue = 5
        self.num_kabe = 1
        self.schedule = RandomActivationByBreed(self)
        #self.schedule = RandomActivation(self)
        self.width = 10
        self.height = 50
        self.space = ContinuousSpace(self.width, self.height, True)
        self.syudan_hito_sita = np.zeros((self.num_agents_sita, 2))
        self.syudan_hito_ue = np.zeros((self.num_agents_ue, 2))
        self.syudan_kabe = np.zeros((self.num_kabe, 2))
        self.kabe_han = 0
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
            self.syudan_kabe = c.naka
            self.kabe_han = c.kabe_iti

            self.schedule.add(c)





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
kabes = model.syudan_kabe
num_kabes = model.num_kabe
kabe_han = model.kabe_han
print("?------------------------",num_kabes,type(num_kabes))

#とりあえず，壁はエージェントとして定義しない
kabe = []


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
    plt.xlim(-10, 50)
    plt.ylim(-20, 90)
    #plt.title("time = "+str(i))
    im_scatter_ue = plt.scatter(im_x_ue, im_y_ue,c="blue")
    im_scatter_sita = plt.scatter(im_x_sita, im_y_sita, c="red")
    ims.append([im_scatter_ue, im_scatter_sita])
    #num_of_huni = 0
    #for j in syudan:
     #   if syudan[j][0] >= 0 and syudan[j][0] <= 10 :
      #      if syudan[j][1] >= 0 and syudan[j][1] <= 60 :
       #         num_of_huni += 1
    #print("範囲内のエージェントは",num_of_huni)

    #if i == 5 :
        #model.make_agents()


   #散布図
    # アニメーション作成

#print(ims)

anim = animation.ArtistAnimation(fig, ims,interval=500)
anim.save('syukatutukareta_anim.gif', writer='writer', fps=4)


plt.show()



