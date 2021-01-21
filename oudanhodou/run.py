import math
import numpy as np
from mesa import Agent, Model
import math
from math import sqrt
import random
from mesa.time import RandomActivation
import matplotlib.pyplot as plt

from oudanhodou import Koutuu

model = Koutuu.Oundahodou
for i in range(20):
    model.step()


