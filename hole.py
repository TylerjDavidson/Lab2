import pygame
from colors import *

class Hole:
	def __init__(self,x,y):
		self.x = x
		self.y = y

	def draw(self,surf):
		r = pygame.Rect((0,0,40,10)) #40x10
		r.center = (self.x,self.y) #set center of rock
		pygame.draw.rect(surf,BLACK,r)
