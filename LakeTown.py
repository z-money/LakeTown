import pygame, sys
from pygame.locals import *
from random import randint
import sqlite3
import MapMaker
import math

class LakeTown:
	def __init__(self, width=1000,height=625):
		pygame.init()
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((self.width,self.height))
		self.screen.fill((255,255,255))
		self.tile_size = 8
		self.LoadTileTable("castle2.png", 8, 8)
		self.water = [(0,48)]
		self.grass = [(4,48),(8,48),(0,44)]

		self.buildMap()

		self.focus = pygame.Rect(-100,-100,8,8)

	def draw(self, x, y, tile):
		self.screen.blit(self.tile_table[tile[0]][tile[1]], (x,y))

	def selectTile(self, loc):
		x = int(math.ceil(loc[0]/8)*8)
		y = int(math.floor(loc[1]/8)*8)

		self.focus.right = x
		self.focus.top = y

	def MainLoop(self):
		LEFT = 1
		RIGHT = 3

		while 1:
			for x in range(int(self.width/8)):
				for y in range(int(self.height/8)):
					if(self.map[x][y]):
						self.draw(x*8, y*8, self.water[0])
					else:
						self.draw(x*8, y*8, self.grass[0])
			if(self.focus != None):
				pygame.draw.rect(self.screen, pygame.Color(0,255,255), self.focus, 1)
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
					lastDown = event.pos
				elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
					if lastDown == event.pos:
						self.selectTile(event.pos)
					else:
						lastDown = None
				elif event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT:
					self.focus = None
				elif event.type == pygame.QUIT:
					sys.exit()
			pygame.display.flip()


	def LoadTileTable(self, filename, width, height):
		image = pygame.image.load(filename).convert()
		image_width, image_height = image.get_size()
		self.tile_table = []
		for tile_x in range(0, int(image_width/width)):
			line = []
			self.tile_table.append(line)
			for tile_y in range(0, int(image_height/height)):
				rect = (tile_x*width, tile_y*height, width, height)
				line.append(image.subsurface(rect))
		return self.tile_table

	def buildMap(self, db_name = 'laketown.db'):
		m = MapMaker.MapMaker(25,25)
		map = m.generateRandomMap()
		self.map = m.simpleEase(map, 5)


