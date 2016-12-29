from random import randint
import math

class MapMaker:
	def __init__(self, width=25,height=25):
		self.width = width
		self.height = height

	def generateMap(self):
		"""pass"""

	def generateRandomMap(self):
		map = []
		for x in range(0,self.width):
			map.append([])
			for y in range(0,self.height):
				map[x].append(randint(0,1))
		self.map = map
		return map

	def simpleEase(self, map, ratio = 2):
		newHeight = len(map[0])*ratio
		newWidth = len(map)*ratio

		newMap = []
		for x in range(0, newWidth):
			newMap.append([])
			for y in range(0, newHeight):
				if(randint(0,10) <= 7):
					newMap[x].append(map[math.floor(x/ratio)][math.floor(y/ratio)])
				else:
					newMap[x].append(int(not(map[math.floor(x/ratio)][math.floor(y/ratio)])))
		
		self.map = newMap
		self.height = newHeight
		self.width = newWidth
		return self.map

	def generateSettlements(self, map, pop_density = 10):
		settlements = []

		for x in range(self.width):
			for y in range(self.height):
				if(row and randint(0,100) <= pop_density):
					settlements.append((x,y))
		self.settlements = settlements
		return settlements



