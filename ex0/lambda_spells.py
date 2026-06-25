from typing import Callable

artifacts: dict[str, int] = [{'name': 'Fire Staff',
                              'power': 71, 'type': 'accessory'},
                             {'name': 'Water Chalice',
                              'power': 108, 'type': 'weapon'},
                             {'name': 'Lightning Rod',
                              'power': 103, 'type': 'armor'},
                             {'name': 'Light Prism',
                              'power': 61, 'type': 'weapon'}]

mages: dict[str, int] = [{'name': 'Phoenix', 'power': 66, 'element': 'lightning'},
         {'name': 'Riley', 'power': 67, 'element': 'lightning'},
         {'name': 'Storm', 'power': 87, 'element': 'lightning'},
         {'name': 'Storm', 'power': 62, 'element': 'ice'},
         {'name': 'Jordan', 'power': 62, 'element': 'shadow'}]

spells = ['freeze', 'shield', 'fireball', 'blizzard']

tri: Callable[[dict], int] = lambda j: j['power']
classement = sorted(artifacts, key=tri, reverse=True)

power: Callable[[dict], int] = lambda j: j['power']
filtre = list(filter(power >= 66, mages))

spe: Callable[[list[str], list[str]]] = lambda j: '* ' + j + ' *'
change = list(map(spe, spells))


calc: Callable[[dict[int, int, float]],] = lambda j: j['power']
fin = max(mages, key=calc)

def mage_stats(mages: dict[str, int]) -> :
