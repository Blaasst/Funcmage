from typing import Callable


def mage_counter() -> Callable:
    count: int = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    def counter(addition: int) -> int:
        nonlocal initial_power
        initial_power += addition
        return initial_power
    return counter


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(name: str) -> int:
        nonlocal enchantment_type
        enchantment_type += ''
        return f"{enchantment_type} {name}"
    return enchantment

def memory_vault() -> dict[str, Callable]:
    memo: dict[str, Callable] = {}
    def store(key: str, value: int) -> None:
        didi: dict[str, int]
        didi[key] = value

    def recall(key: str) -> int | str:
        nonlocal didi
        if didi[key] == {}:
            return "Memory not found"
        else:
            return didi[key]
    memo['store'] = store
    memo['recall' = recall]

if __name__ == "__main__":
    f = mage_counter()
    print(f())
    print(f())
    j = spell_accumulator(10)
    print(j(5))
    print(j(5))
    k = enchantment_factory("Flaming")
    print(k("Blade"))
    print(k("Sword"))

