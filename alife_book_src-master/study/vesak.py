
# coding: utf-8
# Yoshinori Hayakawa
# CDS, Tohoku University

import numpy as np
import random
import math
import pyglet
from pyglet.gl import *

class SDParticle:
    def __init__(self,L):
        x = random.random() * L
        y = random.random() * L
        nx = random.gauss(0,1)
        ny = random.gauss(0,1)
        d = math.sqrt(nx**2 + ny**2)
        nx /= d
        ny /= d
        self.update(x,y,nx,ny)

    def update(self,x,y,nx,ny):
        self.x = x
        self.y = y
        self.nx = nx
        self.ny = ny

class TwoDimField:
    V0=0.2
    ETA=0.2
    def __init__(self,L:int):
        self.L=L
        self.mesh = np.empty((L,L),dtype='object')
        self.list = [ ]
        self.epoch = 0

    def add_particle(self):
        a = SDParticle(self.L)
        ix = int(a.x)
        iy = int(a.y)
        if self.mesh[ix,iy]==None:
            self.mesh[ix,iy] = {a}
        else:
            self.mesh[ix,iy].add(a)
        self.list.append(a)

    def mod_L(self,x):
        if x<0:
            return x+self.L
        elif x>=self.L:
            return x-self.L
        else:
            return x

    def diff(self,d):
        if d > self.L/2:
            return self.L-d
        elif d < -self.L/2:
            return d + self.L
        else:
            return d

    def move(self,particle):
        ix = int(particle.x)
        iy = int(particle.y)
        sx = 0.0
        sy = 0.0
        for i in range(ix-1,ix+2,1):
            k = self.mod_L(i)
            for j in range(iy-1,iy+2,1):
                ell = self.mod_L(j)
                neighbors = self.mesh[k,ell]
                if neighbors == None:
                    continue
                for p in neighbors:
                    if self.diff(particle.x - p.x)**2 + self.diff(particle.y - p.y)**2 < 1.0:
                        sx += p.nx
                        sy += p.ny

        s=math.sqrt(sx**2+sy**2)
        sx /= s
        sy /= s
        xi = TwoDimField.ETA * random.uniform(-0.5*math.pi,0.5*math.pi)
        nx2 = sx * math.cos(xi) - sy * math.sin(xi)
        ny2 = sx * math.sin(xi) + sy * math.cos(xi)

        x2 = self.mod_L(particle.x + nx2 * TwoDimField.V0)
        y2 = self.mod_L(particle.y + ny2 * TwoDimField.V0)
        if ix != int(x2) or iy != int(y2):
            self.mesh[ix,iy].remove(particle)
            if self.mesh[int(x2),int(y2)] == None:
                self.mesh[int(x2),int(y2)] = {particle}
            else:
                self.mesh[int(x2),int(y2)].add(particle)
        particle.update(x2,y2,nx2,ny2)

    def update(self):
        particle = random.choice(self.list)
        self.move(particle)
        dt = 1.0/len(self.list)
        self.epoch += dt

    def order_param(self):
        sx=0
        sy=0
        for p in self.list:
            sx += p.nx
            sy += p.ny
        return math.sqrt(sx**2+sy**2)/len(self.list)

###
L = 64
SCALE = 8
config = pyglet.gl.Config(double_buffer=True)
win = pyglet.window.Window(L*SCALE,L*SCALE,config=config,resizable=False)
win.set_caption('Vicsek Model')

@win.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(0,0,0,1)
    redraw()

def next_frame(dt):
    return

def redraw():
    for cnt in range(1000):
        f.update()
    for particle in f.list:
        glColor3d(0.8,0.3,0.1)
        glLineWidth(SCALE/4)
        glBegin(GL_LINES)
        glVertex2d(particle.x*SCALE, particle.y*SCALE)
        glVertex2d(particle.x*SCALE + particle.nx*SCALE, particle.y*SCALE + particle.ny*SCALE)
        glEnd()

    str = 'T={0:.1f} Q={1:1.3f}'.format(f.epoch,f.order_param())
    label = pyglet.text.Label(str,
                              font_name='Helvetica', color=(255,255,255,255),
                              font_size=12, x=10, y=10)
    label.draw()


f = TwoDimField(L)
for k in range(1000):
    f.add_particle()

pyglet.clock.schedule_interval(next_frame, 1/20.0)
pyglet.app.run()