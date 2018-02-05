#!/usr/bin/py

import sys
import pygame
import serial
from pygame.locals import *
import math
import Launcher


pygame.init()

DISPLAYSURF = pygame.display.set_mode((500,400)) #main window
pygame.display.set_caption("Launcher") #window title
#s = serial.Serial("/dev/ttyACM0") #uncomment eventually
FPS = 30 #frames/s



def draw_world(surf): #background function
  fontObj = pygame.font.Font('freesansbold.ttf',32) #font and font size
  textSurfaceObj = fontObj.render('Launcher 1.0',True,(255,255,255),(0,0,0)) #white text, black highlight
  textRectObj = textSurfaceObj.get_rect()
  textRectObj.center = (250,20)
  pygame.draw.rect(surf,(20,150,200),(0,0,500,380)) #sky
  pygame.draw.rect(surf,(0,255,20),(0,380,500,20)) #grass
  (surf).blit(textSurfaceObj,textRectObj) #draw title text

while(True): #main loop
  draw_world(DISPLAYSURF) #draw background
  


  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP: #rotate up
        Launcher.changeAngle(3)
      if event.key == pygame.K_DOWN: #rotate down
        Launcher.changeAngle(-3)
      if event.key == pygame.K_LEFT: #decrease power
        Launcher.changeMagnitude(-5)
      if event.key == pygame.K_RIGHT: #increase power
        Launcher.changeMagnitude(5)
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  Launcher.drawCanon(DISPLAYSURF) #display Launcher  
  pygame.display.update()
  fpsClock.tick(FPS)



      
         



