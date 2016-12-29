import sqlite3, uuid

def reset_table(c, table):
	c.execute('DELETE FROM %s' % table)

def add_race(c, race):
	c.execute('INSERT INTO race(name) VALUES (\'%s\')' % race)

def add_profession(c, profession):
	c.execute('INSERT INTO profession(name) VALUES (\'%s\')' % profession)

def add_biome(c, biome):
	c.execute('INSERT INTO biome(name) VALUES(\'%s\')' % biome)

def add_settlement(c, biome):
	c.execute('INSERT INTO settlement(name) VALUES(\'%s\')' % settlement)

conn = sqlite3.connect('laketown.db')

c = conn.cursor()

reset_table(c, 'race')
reset_table(c, 'profession')
reset_table(c, 'biome')
reset_table(c, 'settlement')

races = ['orc', 'elf', 'human', 'goblin', 'giant', 'troll', 'minotaur', 'dragon', 'beast', 'wyrm', 'dwarf', 'halfling', 'centaur', 'vampire', 'dryad']
for race in races:
	add_race(c, race)

professions = ['warrior', 'mage', 'rogue', 'archer', 'paladin', 'priest', 'necromancer', 'dragon_rider', 'dragon_hunter', 'summoner', 'trader', 'hunter', 'guard', 'worker']
for profession in professions:
	add_profession(c, profession)

biomes = ['desert', 'forest', 'plains', 'marsh', 'tundra', 'mountains', 'plains', 'glacier', 'jungle', 'volcano', 'ocean', 'coast']
for biome in biomes:
	add_biome(c, biome)

settlements = ['village', 'trading_post', 'castle', 'mine', 'hideout', 'camp', 'logging_camp', 'hunting_camp', 'temple', 'city', 'town']
for settlement in settlements:
	add_settlement(c, settlement)

conn.commit()
conn.close()