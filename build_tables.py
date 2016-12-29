import sqlite3

conn = sqlite3.connect('laketown.db')

c = conn.cursor()

c.execute('DROP TABLE IF EXISTS race')
c.execute('CREATE TABLE race(id INTEGER PRIMARY KEY, name INTEGER)')

c.execute('DROP TABLE IF EXISTS profession')
c.execute('CREATE TABLE profession(id INTEGER PRIMARY KEY, name INTEGER)')

c.execute('DROP TABLE IF EXISTS biome')
c.execute('CREATE TABLE biome(id INTEGER PRIMARY KEY, name INTEGER)')

c.execute('DROP TABLE IF EXISTS settlement')
c.execute('CREATE TABLE settlement(id INTEGER PRIMARY KEY, name INTEGER)')

conn.commit()
conn.close()