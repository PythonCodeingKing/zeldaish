import pygame
import random

class Enemy:

	def __init__(self, screen, tiles, player):
		self.nimage = pygame.image.load("other\\enemy.png")
		self.limage = pygame.image.load("other\\lenemy.png")
		self.image = self.nimage
		self.rect = self.image.get_rect()
		self.screen = screen
		self.playerobj = player
		self.looking_left = False
		self.player = player.rect
		self.dImage = pygame.image.load("other\\dEnemy.png")
		self.rect.x = 120
		random.seed()
		self.heath = 5
		# the ai type of the enemy
		# 0 = normal
		# 1 = 'noob' (random movement)
		# 2 = 'tryhard' (little bit more health)
		# 3 = 'evade'
		self.type = random.randint(0, 30)
		self.rect.y = 120
		self.tiles = tiles
		self.health = 5
		if self.type < 20:
				self.health = 7
		self.isDamage = False
		if self.playerobj.hasBombs:
			self.drop = 2
		else:
			self.drop = 1
		self.current_tile = self.tiles[self.rect.y//40][self.rect.x//40].type
	def get_current_tile(self):
		self.current_tile = self.tiles[self.rect.y//40][self.rect.x//40].type
		#print(self.current_tile)
	def update(self):
		self.get_current_tile()
		if self.type < 10 or self.type > 20:
			if self.player.x < self.rect.x:
				self.rect.x -= 40
				if self.current_tile == "tree":
					self.rect.x += 40
			if self.player.x > self.rect.x:
				self.rect.x += 40
				if self.current_tile == "tree":
					self.rect.x -= 40
			if self.player.y < self.rect.y:
				self.rect.y -= 40
				if self.current_tile == "tree":
					self.rect.y += 40

			if self.player.y > self.rect.y:
				self.rect.y += 40
		if self.type > 10 and self.type < 20:
			direction = random.randint(0, 3)
			if direction == 0:
				self.rect.x += 40
			if direction == 1:
				self.rect.x -= 40
			if direction == 2:
				self.rect.y += 40
			if direction == 3:
				self.rect.y -= 40
		if self.health <= 0:
			if self.drop == 1 and self.playerobj.health > 0:
				self.playerobj.health += random.randint(0, 5-self.playerobj.health)
			if self.drop == 2:
				self.playerobj.bombs += random.randint(0, 15-self.playerobj.bombs)
			return 1
		else:
			return 0
	def draw(self):
		self.screen.blit(self.image, self.rect)
