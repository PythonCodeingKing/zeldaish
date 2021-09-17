import pygame

class Item:
	def __init__(self, image, x, y, id, player):
		self.image = pygame.image.load(image)
		self.x, self.y = x, y
		self.player = player
		self.id = id
	def draw(self, screen):
		screen.blit(self.image, (self.x, self.y))

	def onPlayerCollision(self):
		pygame.mixer.music.load("other\\itempickup.wav")
		pygame.mixer.music.play(1)
		if self.id == 1:
			self.player.hasSnorkel = True
		if self.id == 2:
			self.player.hasMachete = True
			self.player.attack_damage = 5
		if self.id == 3:
			self.player.hasBombs = True
			self.player.bombs = 15