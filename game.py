#!/usr/bin/py

import sys
import pygame
import serial
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500,400)) #window size
pygame.display.set_caption("Launchr") #window title
#s = serial.Serial("/dev/ttyACM0") #uncomment eventually
FPS = 30 #frames/s

fontObj = pygame.font.Font('freesansbold.ttf',32) #font and font size
textSurfaceObj = fontObj.render('Launchr 1.0',True,(255,255,255),(0,0,0)) #white text, black highlight
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (250,20)

def draw_world(surf): #background function
  pygame.draw.rect(surf,(20,150,200),(0,0,500,380)) #sky
  pygame.draw.rect(surf,(0,255,20),(0,380,500,20)) #grass



while True: #main loop
  draw_world(DISPLAYSURF) #draw background
  DISPLAYSURF.blit(textSurfaceObj,textRectObj) #draw text

  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit() 
  pygame.display.update()

=======
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
>>>>>>> 9bae46b64e7032ac45e09bd0ccc61174a23ad48a
