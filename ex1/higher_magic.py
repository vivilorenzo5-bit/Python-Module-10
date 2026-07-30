from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        res1 = spell1(target, power)
        res2 = spell2(target, power)
        return res1, res2
    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional_spell(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence_spell(target: str, power: int) -> list[str]:
        return [s(target, power) for s in spells]
    return sequence_spell


if __name__ == "__main__":
    test_values: list = [16, 5, 15]
    targets: list = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def is_strong(target: str, power: int) -> bool:
        return power >= 20

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: \n{combined(targets[0], test_values[0])}")
    res1, res2 = combined(targets[0], test_values[0])
    print(f"\nCombined spell result (diff output cooler): \n{res1}, {res2}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball(targets[1], test_values[1])}")
    print(f"Amplified: {mega_fireball(targets[1], test_values[1])}")

    print("\nTesting conditional caster...")
    strong_cast = conditional_caster(is_strong, fireball)
    print(f"Power 25: {strong_cast(targets[2], 25)}")
    print(f"Power 10: {strong_cast(targets[2], 10)}")

    print("\nTesting spell sequence...")
    combo = spell_sequence([fireball, heal])
    print(f"Sequence result: {combo(targets[3], test_values[2])}")
