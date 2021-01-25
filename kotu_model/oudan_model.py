import numpy as np
from mesa import Agent, Model
import math
import random
from mesa.time import SimultaneousActivation
import matplotlib.pyplot as plt
#from  hulistics.hulistics_01 import kakudo
from hulistics_01 import kakudo, kakudo_kai,kakudo_kai_ue

from mesa.space import ContinuousSpace
from scipy import optimize
import matplotlib.animation as animation
from agent_sita import Hokousya_sita
from agent_ue import Hokousya_ue




class Oundahodou(Model):
    """これはモデル　連続空間に配置する"""

    def __init__(self):
        self.num_agents_sita = 20
        self.num_agents_ue = 20
        self.num_kabe = 1
        self.schedule = SimultaneousActivation(self)
        self.width = 10
        self.height = 50
        self.space = ContinuousSpace(self.width, self.height, True)
        self.syudan_hito_sita = np.zeros((self.num_agents_sita, 2))
        self.syudan_hito_ue = np.zeros((self.num_agents_ue, 2))
        self.syudan_kabe = np.zeros((self.num_kabe, 2))
        self.time = 1000
        self.sonzai_ue = np.array([])
        self.sonzai_sita = np.array([])
        # Create agents エージェントは存在した

        self.im_x_sita = []
        self.im_y_sita = []

        self.im_x_ue = []
        self.im_y_ue = []

        for j in range(self.num_agents_sita):
            a = Hokousya_sita(j, self)
            self.syudan_hito_sita[j,0] = a.iti_x
            self.syudan_hito_sita[j,1] = a.iti_y
            self.schedule.add(a)
            self.sonzai_sita = np.append(self.sonzai_sita, j)
            print(a.unique_id,"の下から来るエージェントは生成されました")
            #self.syudan_hito_sita[i,0] = a.iti_x
            #self.syudan_hito_sita[i,1] = a.iti_y

        for i in range(self.num_agents_ue):
            b = Hokousya_ue(i, self)
            self.syudan_hito_ue[i, 0] = b.iti_x
            self.syudan_hito_ue[i, 1] = b.iti_y
            self.schedule.add(b)
            self.sonzai_ue = np.append(self.sonzai_ue,i)
            #self.syudan_hito_ue[i,0] = b.iti_x
            #self.syudan_hito_ue[i,1] = b.iti_y


        #壁を作る
        #for i in range(self.num_kabe):
            #c = Kabe(i, self)
            #self.schedule.add(c)
            #self.syudan_kabe[i, 0] = c.iti[0]
            #self.syudan_kabe[i, 1] = c.iti[1]




    def make_agents(self):
        """途中からアクティブになるエージェントの作成"""

    def step(self):
        '''Advance the model by one step.'''
        self.im_x_sita = []
        self.im_y_sita = []

        self.im_x_ue = []
        self.im_y_ue = []

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
