from classes import Car, Jet, Ship

ship = Ship('V5', 'Mercury', 1_000_000, 1995, 80, 40)
ship.TONNAGE = 1_000_000
ship.ENVIRONMENT = 'marine'
ship.WEIGHT = 2_000_000
ship.SOUND = 'tooo'
ship.FUEL_TANK = 1000
ship.alarm()
print(ship)
ship.make_sound()
ship.get_features()