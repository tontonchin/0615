import numpy as np
from mesa import Agent, Model
import math
import random
from mesa.time import SimultaneousActivation
import matplotlib.pyplot as plt
#from  hulistics.hulistics_01 import kakudo
#from hulistics.hulistics_02 import plot2d, hito_sesyoku, kabe_sessyoku, func_hulistics_2
#from hulistics.syuuino import syuui1,syuui2,hankai,han_kyori
from mesa.space import ContinuousSpace
from scipy import optimize
import matplotlib.animation as animation
from agent_sita import Hokousya_sita
from agent_ue import Hokousya_ue
from oudan_model import Oundahodou
import sys



model = Oundahodou()
#print(model)

syudan = model.dasu_syudan_hito()
print("エージェントの集団です",syudan)
num_agents = model.num_agents_ue + model.num_agents_sita
print("num_agent",num_agents)
kabes = model.dasu_nu_kabe()
num_kabes = model.num_kabe
print("?------------------------",num_kabes,type(num_kabes))

#print("そんざいしているのかうえ",model.sonzai_ue)
#print("そんざいしているのかした",model.sonzai_sita)


print("最初のIm_x_ue", model.im_x_ue)


fig = plt.figure()
ims = []

im_x_sita = []
im_y_sita = []

im_x_ue = []
im_y_ue = []


for i in range(30):
    #im_x_sita = []
    #im_y_sita = []
    #im_x_ue = []
    #im_y_ue = []
    #print("im",im_x,im_y,"HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
    #im_scatter = plt.scatter(im_x, im_y)
    #ims.append(im_scatter)
    print(i,"ステップ目","&^&*(&^*(&^(*&^*&(^&(*^(&*%^&*(^&*(%^&*%&(*^%&^%(^")
    model.step()
    #print("im", im_x, im_y,"HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
    #print("im_len",len(im_x))
    im_scatter_sita = plt.scatter(im_x_sita, im_y_sita,c="red")
    im_scatter_ue = plt.scatter(im_x_ue, im_y_ue, c="blue")
    print("im_scatter_sita",im_x_sita)
    ims.append([im_scatter_sita,im_scatter_ue])
    print(i,"ステップ目","syudan",syudan)
    print("im_x_sita",im_x_sita)
    im_x_sita = []
    im_y_sita = []
    im_x_ue = []
    im_y_ue = []



   #散布図
    # アニメーション作成

#print(ims)

anim = animation.ArtistAnimation(fig, ims,interval=500)
anim.save('kotu_1225_anim.gif', writer='writer', fps=4)
#anim.save('a2.gif')

plt.show()
