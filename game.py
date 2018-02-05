#!/usr/bin/py

import sys
import pygame
import serial
from pygame.locals import *
import math
import Launcher


pygame.init()

DISPLAYSURF = pygame.display.set_mode((500,400)) #window size
pygame.display.set_caption("Launchr") #window title
#s = serial.Serial("/dev/ttyACM0") #uncomment eventually
FPS = 30 #frames/s



def draw_world(surf): #background function
  fontObj = pygame.font.Font('freesansbold.ttf',32) #font and font size
  textSurfaceObj = fontObj.render('Launchr 1.0',True,(255,255,255),(0,0,0)) #white text, black highlight
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (250,20)
  pygame.draw.rect(surf,(20,150,200),(0,0,500,380)) #sky
  pygame.draw.rect(surf,(0,255,20),(0,380,500,20)) #grass


while True: #main loop
  draw_world(DISPLAYSURF) #draw background
  DISPLAYSURF.blit(textSurfaceObj,textRectObj) #draw title text


  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        Launcher.changeAngle(3)
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  Launcher.draw(DISPLAYSURF) #display Launcher  
  pygame.display.update()
  fpsClock.tick(FPS)



      
         



