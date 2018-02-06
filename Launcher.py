#!/usr/bin/py
import math
import pygame
from pygame.locals import *

MAX_MAG = 100
MIN_MAG = 10
MAX_ANGLE = 90
MIN_ANGLE = 0


class launcher:

	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.magnitude = 50
		self.angle = math.radians(45)

	def changeMagnitude(self,delta):
		if self.magnitude+delta > MAX_MAG:
			delta = 0
		elif self.magnitude+delta < MIN_MAG:
			delta = 0
		self.magnitude += delta

	def changeAngle(self,dtheta):
		if math.degrees(self.angle+math.radians(dtheta)) > 90:
			dtheta = 0
		elif math.degrees(self.angle+math.radians(dtheta)) <0:
			dtheta = 0
		self.angle = self.angle + math.radians(dtheta)

	def drawCannon(self,surf):
		X1 = self.x + self.magnitude*math.cos(self.angle) 
		Y1 = self.y - self.magnitude*math.sin(self.angle)
		pygame.draw.line(surf,(255,0,0),(self.x,self.y),(X1,Y1),8)



#Starting at (0,380)
#r = 10
#theta = 45
# x1 =x0 + mag*cos(theta)
# Y1 =Y0 - mag*sin(theta) 
