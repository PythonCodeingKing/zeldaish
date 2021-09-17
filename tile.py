import pygame

class Tile:
	def __init__(self, texture, x, y, screen):
		self.image = pygame.image.load(texture)
		self.type = texture[6:]
		self.type = self.type[:4]
		self.x, self.y = x, y
		self.screen = screen
		self.calculate()
	def calculate(self):
		self.rX = self.x*40
		self.rY = self.y*40

	def specialType(self, ntype):
		self.type = ntype
		self.type = self.type[0:4]

	def draw(self):
		self.screen.blit(self.image, (self.rX, self.rY))
		