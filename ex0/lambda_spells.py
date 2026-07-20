
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


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    classement = sorted(artifacts, key=lambda j: j['power'], reverse=True)
    return classement


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtre = list(filter(lambda j: j['power'] >= min_power, mages))
    return filtre


def spell_transformer(spells: list[str]) -> list[str]:
    change = list(map(lambda j: '* ' + j + ' *', spells))
    return change


def mage_stats(mages: list[dict]) -> dict:
    fatigue: dict = []
    maxi = max(mages, key=lambda j: j['power'])
    mini = min(mages, key=lambda j: j['power'])
    moyenne = sum(map(lambda j: j['power'], mages)) / len(mages)

    fatigue['maxi', maxi]
    fatigue['mini', mini]
    fatigue['moyenne', moyenne]
    return fatigue


def main(mages: list[dict], spells: list[str],
         artifacts: list[dict]) -> None:
    print("===Testing artifact sorter===")
    print("Before sorting:")
    print(artifacts)
    print("Sorting list...")
    print(artifact_sorter(artifacts))
    print("\n==============================")
    print("===Testing power filter===")
    print("Before filter:")
    print(mages)
    print("filtering mages...")
    print(power_filter(mages, 66))
    print("\n==============================")
    print("===Testing spell transformer===")
    print("Before transformation:")
    print(spells)
    print("transforming spells...")
    print(spell_transformer(spells))
    print("\n==============================")
    print("===Testing mage stats===")
    print(mage_stats(mages))
    print("\n==============================")


if __name__ == "__main__":
    main(mages, spells, artifacts)
