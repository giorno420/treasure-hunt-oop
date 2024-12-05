import time

rucksack = []
health = 20


class Enemy:
    def __init__(self, name, max_health, damage):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.damage = damage

class Place:
    def __init__(self, connections, items):
        self.connections = connections
        self.items = items
    # entrance requirement
    
    # 
    
class Item:
    def __init__(self, name, item_type, durability):
        self.name = name
        self.itemtype = item_type
        self.durability = durability
    
    # item functions too
