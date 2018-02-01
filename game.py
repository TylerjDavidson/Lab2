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

