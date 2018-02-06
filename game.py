#!/usr/bin/py

import pygame, sys
import serial
from pygame.locals import *
import math
import Launcher

def draw_world(surf):
	fontObj = pygame.font.Font('freesansbold.ttf',32) #font and font size
	textSurfaceObj = fontObj.render('Launcher 1.0',True,(255,255,255),(0,0,0)) #white text, black highlight
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (250,20)
	pygame.draw.rect(surf,(20,150,200),(0,0,500,380)) #sky
	pygame.draw.rect(surf,(0,255,20),(0,380,500,20)) #grass
	(surf).blit(textSurfaceObj,textRectObj) #draw title text

pygame.init() 
DISPLAYSURF = pygame.display.set_mode((500,400)) #main window
#s = serial.Serial("/dev/ttyACM0") #uncomment eventually
FPS = 30 #frames/s
fpsClock = pygame.time.Clock()
Launcher1 = Launcher.launcher(0,380)

while(True):
	draw_world(DISPLAYSURF) #draw background
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP: 
				#rotate up
				Launcher1.changeAngle(3)
			if event.key == pygame.K_DOWN: 
				#rotate down
				Launcher1.changeAngle(-3)
			if event.key == pygame.K_LEFT:
				#decrease power
				Launcher1.changeMagnitude(-5)
			if event.key == pygame.K_RIGHT:
				#increase power
				Launcher1.changeMagnitude(5)
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	Launcher1.drawCannon(DISPLAYSURF) #display Launcher  
	pygame.display.update()
	fpsClock.tick(FPS)








