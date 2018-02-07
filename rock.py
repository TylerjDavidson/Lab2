import pygame
from colors import *

class Rock:
	def __init__(self,x,y):
		self.x = x
		self.y = y
		self.v_x = 0
		self.v_y = 0
		
	def move(self,time):
		self.x = self.x + self.v_x*time
		self.y = self.y - self.v_y*time

	def isMoving(self):
		return self.v_x != 0 or self.v_y != 0
	
	def draw(self,surf):
		r = pygame.Rect((0,0,10,10)) #10x10 rectangle
		r.center = (self.x,self.y) #set center of rock
		pygame.draw.rect(surf,ROCK_COLOR,r)
		


