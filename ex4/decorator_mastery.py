import functools
import time
from typing import Any, Callable


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print(f"Spell completed in {elapsed_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = kwargs.get('power')
            if power is None:
                for arg in args:
                    if isinstance(arg, int):
                        power = arg
                        break
            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attemps: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attemps + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attemps:
                        print(
                            f"Spell failed, retrying... (attempt {attempt}/"
                            f"{max_attemps}"
                        )
            return f"Spell casting failed after {max_attemps} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if not isinstance(name, str) or len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.1)
        return "Fireball cast!"
    print(f"Result: {fireball()}")

    print("\nTesting power validator alone...")

    @power_validator(min_power=20)
    def cast_fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} with {power} power!"
    print(cast_fireball("Dragon", 25))
    print(cast_fireball("Dragon", 10))

    print("\nTesting retrying spell...")

    def test_retry() -> None:
        attempts_count = 0

        @retry_spell(max_attemps=3)
        def unstable_spell() -> str:
            nonlocal attempts_count
            attempts_count += 1
            if attempts_count < 4:
                raise ValueError("Magic overload!")
            return "Success!"

        print(unstable_spell())
    test_retry()

    print("\nTesting MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf The Grey"))
    print(MageGuild.validate_mage_name("A1"))

    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Firebolt", 5))
