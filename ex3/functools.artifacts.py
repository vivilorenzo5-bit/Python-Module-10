from collections.abc import Callable
import functools
import operator
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    ops: dict[str, Callable[[int, int], int]] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire": functools.partial(base_enchantment, 50, "fire"),
        "ice": functools.partial(base_enchantment, 50, "ice"),
        "lightning": functools.partial(base_enchantment, 50, "lightning")
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def dispatcher(spell: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage"

    @dispatcher.register(str)
    def _(spell: int) -> str:
        return f"Enchantment: {spell}"

    @dispatcher.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell)} spells"

    return dispatcher


if __name__ == "__main__":
    print("Testing spell reducer...")
    powers = [10, 20, 30, 40]
    print(f"Sum: {spell_reducer(powers, 'add')}")
    print(f"Product: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")

    print("\nTesting partial enchanter...")

    def base_enchant(power: int, element: str, target: str) -> str:
        return f"Enchanted {target} with {power} {element} magic"
    enchanters = partial_enchanter(base_enchant)
    print(enchanters["fire"]("Sword"))
    print(enchanters["ice"]("Shield"))

    print("\nTesting memoied fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")
    print(f"Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    cast = spell_dispatcher()
    print(cast(42))
    print(cast("fireball"))
    print(cast(["fireball", "heal", "shield"]))
    print(cast(4.2))
