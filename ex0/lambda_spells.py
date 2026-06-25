
artifacts: list[dict] = [{'name': 'Fire Staff',
                         'power': 71, 'type': 'accessory'},
                         {'name': 'Water Chalice',
                         'power': 108, 'type': 'weapon'},
                         {'name': 'Lightning Rod',
                         'power': 103, 'type': 'armor'},
                         {'name': 'Light Prism',
                         'power': 61, 'type': 'weapon'}]

mages: list[dict] = [{'name': 'Phoenix', 'power': 66, 'element': 'lightning'},
                     {'name': 'Riley', 'power': 67, 'element': 'lightning'},
                     {'name': 'Storm', 'power': 87, 'element': 'lightning'},
                     {'name': 'Storm', 'power': 62, 'element': 'ice'},
                     {'name': 'Jordan', 'power': 62, 'element': 'shadow'}]

spells = ['freeze', 'shield', 'fireball', 'blizzard']

classement = sorted(artifacts, key=lambda j: j['power'], reverse=True)

filtre = list(filter(lambda j: j['power'] >= 66, mages))


change = list(map(lambda j: '* ' + j + ' *', spells))

maxi = max(mages, key=lambda j: j['power'])
mini = min(mages, key=lambda j: j['power'])
moyenne = sum(map(lambda j: j['power'], mages)) / len(mages)


def main(mages: list[dict], spells: list[str],
         artifacts: list[dict]) -> None:
    print("===Testing artifact sorter===")
    print("Before sorting:")
    print(artifacts)
    print("Sorting list...")
    print(classement)
    print("\n==============================")
    print("===Testing power filter===")
    print("Before filter:")
    print(mages)
    print("filtering mages...")
    print(filtre)
    print("\n==============================")
    print("===Testing spell transformer===")
    print("Before transformation:")
    print(spells)
    print("transforming spells...")
    print(change)
    print("\n==============================")
    print("===Testing mage stats===")
    print(f"max is : {maxi['power']}")
    print(f"min is : {mini['power']}")
    print(f"Average is: {moyenne}")
    print("\n==============================")


if __name__ == "__main__":
    main(mages, spells, artifacts)
