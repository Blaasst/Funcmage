from collections.abc import Callable


test_values = [14, 22, 9]
test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']


def spell(target: str, power: int) -> str:
    if power < 15:
        return f"I use fireball on {target}"
    elif power == 15:
        return f"I use big fireball on {target}"
    elif power > 15:
        return f"I use Massive destroyer on {target}"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(t1: str, p1: int) -> tuple[str, str]:
        ok: str = spell1(t1, p1)
        ko: str = spell2(t1, p1)
        return (ok, ko)
    return combined_spell


def power_amplifier(spell1: Callable, multiplier: int) -> Callable:
    def spell_amplified(target: str, power: int) -> str:
        ok: str = spell1(target, power * multiplier)
        return ok
    return spell_amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def condspell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"
    return condspell


def check(target: str, power: int) -> bool:
    if power > 14:
        return True
    else:
        return False


def spell_sequence(spells: list[Callable]) -> Callable:
    def multispell(target: str, power: int) -> list[str]:
        gl: list[str] = []
        for el in spells:
            gl.append(el(target, power))
        return gl
    return multispell


def main() -> None:
    combinaison: Callable = spell_combiner(spell, heal)
    ampli: Callable = power_amplifier(spell, 3)
    cond: Callable = conditional_caster(check, spell)
    multi: Callable = spell_sequence((spell, spell, heal, spell, heal))
    print("testing combination...")
    print(combinaison('wizard', 15))
    print('\n')
    print("testing amplification...")
    print(ampli('wizard', 15))
    print('\n')
    print("testing conditionning...")
    print(cond('wizard', 15))
    print(cond('wizard', 13))
    print('\n')
    print("testing sequencing...")
    print(multi('wizard', 15))


if __name__ == '__main__':
    main()
