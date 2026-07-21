from typing import Any

artifacts: list[dict[Any, Any]] = [{'name': 'Fire Staff',
                                   'power': 71, 'type': 'accessory'},
                                   {'name': 'Water Chalice',
                                   'power': 108, 'type': 'weapon'},
                                   {'name': 'Lightning Rod',
                                   'power': 103, 'type': 'armor'},
                                   {'name': 'Light Prism',
                                   'power': 61, 'type': 'weapon'}]

mages: list[dict[Any, Any]] = [
                     {'name': 'Phoenix', 'power': 66, 'element': 'lightning'},
                     {'name': 'Riley', 'power': 67, 'element': 'lightning'},
                     {'name': 'Storm', 'power': 87, 'element': 'lightning'},
                     {'name': 'Storm', 'power': 62, 'element': 'ice'},
                     {'name': 'Jordan', 'power': 62, 'element': 'shadow'}]

spells: list[str] = ['freeze', 'shield', 'fireball', 'blizzard']


def artifact_sorter(artifacts: list[dict[Any, Any]]) -> list[dict[Any, Any]]:
    classement = sorted(artifacts, key=lambda j: j['power'], reverse=True)
    return classement


def power_filter(mages: list[dict[Any, Any]],
                 min_power: int) -> list[dict[Any, Any]]:
    filtre = list(filter(lambda j: j['power'] >= min_power, mages))
    return filtre


def spell_transformer(spells: list[str]) -> list[str]:
    change = list(map(lambda j: '* ' + j + ' *', spells))
    return change


def mage_stats(mages: list[dict[Any, Any]]) -> dict[Any, Any]:
    fatigue: dict[Any, Any] = {}
    maxi = max(mages, key=lambda j: j['power'])
    mini = min(mages, key=lambda j: j['power'])
    moyenne = sum(map(lambda j: j['power'], mages)) / len(mages)

    fatigue = {"maxi": maxi, 'mini': mini, 'moyenne': moyenne}
    return fatigue


def main(mages: list[dict[Any, Any]], spells: list[str],
         artifacts: list[dict[str, int]]) -> None:
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
