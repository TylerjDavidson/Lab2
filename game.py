#!/usr/bin/py
import math
import math.sin
import math.cos

MAX_MAG = 100
MIN_MAG = 10
MAX_ANGLE = 90
MIN_ANGLE = 0


class launcher:
  
  def __init__(self,x,y):
     self.x = x
     self.y = y
     self.magnitude = 50
     self.angle = 45
   
  def changeMagnitude(self,delta):
    if delta <= 100 and delta >= 10
      self.magnitude = self.magnitude + delta 
    else 
      delta = 0
      self.magnitude = self.magnitude + delta

  def changeAngle(self,dtheta):
    if dtheta <= 90 and dtheta >= 0
      self.angle = self.angle + dtheta
    else
      dtheta = 0
      self.angle = self.angle + dtheta

  def drawCannon(self,surf)
    X1 = x + self.magnitude*cos(self.theta)
    Y1 = y + self.magnitude*sin(self.theta)
      
         

#Starting at (0,380)
#r = 10
#theta = 45
# x1 =x0 + mag*cos(theta)
# Y1 =Y0 - mag*sin(theta) 
