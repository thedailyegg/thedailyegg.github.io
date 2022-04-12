from browser import document, window

from math import atan, degrees
from random import random

page = document["page"]

class Dynamic():
    def __init__(self, element, page=page):
        self.element = element
        self.x = 50
        self.y = 50
        self.dx = -50
        self.dy = 500
        self.gravity = 0.2
        self.damping = 0.8
        self.y_damping = self.damping
        self.x_damping = self.damping
        self.ang = 0
        self.arena_width = page.width-150
        self.arena_height =page.height-100
        print(page.width)
        print(page.height)
        self.x = 0
        self.y = 0

    def damp(self):
        self.dx *= self.x_damping
        self.dy *= self.y_damping
    def render(self):
        self.element.style.transform = f"translate({self.x}px,{self.y}px) rotate({self.angle()}deg)"
        self.x += self.dx
        self.y += self.dy
        if self.x>=self.arena_width: # right wall
            self.damp()
            self.x = self.arena_width
            self.dx *= -1 
        if self.x<=0: # left wall
            self.damp()
            self.x = 0
            self.dx *= -1
        if self.y >= self.arena_height:# floor
            self.y = self.arena_height
            self.damp()
            self.dy *= -1
        if self.y <= 0:# ceiling
            self.damp()
            self.y = 0
            self.dy *= -1
        self.dy+=self.gravity
    def angle(self):
        # angles are clockwise so god help me
        if self.dx>0:
            if self.dy>0:# quadrant 4
                self.ang = 90 + degrees( atan(self.dy/self.dx) )
            elif self.dy<0:# quadrant 1
                self.ang = degrees( atan(self.dx/-self.dy) )
            else: return self.ang
        elif self.dx<0:
            if self.dy>0: # quadrant 3
                self.ang = 180 + degrees( atan(-self.dx/self.dy) )
            elif self.dy<0: # quadrant 2
                self.ang = 270 + degrees( atan(-self.dy/-self.dx) )
            else: return self.ang
        else: return self.ang
        return self.ang

egg = Dynamic(document["egg"])

def animloop(t):
    global run, egg
    run = window.requestAnimationFrame(animloop)
    egg.render()

run = window.requestAnimationFrame(animloop)