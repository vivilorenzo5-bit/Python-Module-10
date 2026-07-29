def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    max_p = max(mages, key=lambda m: m['power'])['power']
    min_p = min(mages, key=lambda m: m['power'])['power']
    total_p = sum(map(lambda m: m['power'], mages))
    avg_p = round(total_p / len(mages), 2)

    return {
        'max_power': max_p,
        'min_power': min_p,
        'avg_power': avg_p
    }


if __name__ == "__main__":
    artifacts = [{'name': 'Shadow Blade', 'power': 100, 'type': 'relic'},
                 {'name': 'Ice Wand', 'power': 114, 'type': 'focus'},
                 {'name': 'Water Chalice', 'power': 86, 'type': 'armor'},
                 {'name': 'Storm Crown', 'power': 100, 'type': 'focus'}]
    mages = [{'name': 'Rowan', 'power': 72, 'element': 'lightning'},
             {'name': 'Phoenix', 'power': 97, 'element': 'lightning'},
             {'name': 'Luna', 'power': 75, 'element': 'lightning'},
             {'name': 'Zara', 'power': 85, 'element': 'water'},
             {'name': 'Jordan', 'power': 61, 'element': 'water'}]
    spells = ['tornado', 'flash', 'earthquake', 'fireball']

    print("Testing artifact sorter...")
    sorted_arts = artifact_sorter(artifacts)
    print(f"{sorted_arts}")
    print(f"{sorted_arts[0]['name']} ({sorted_arts[0]['power']} power) "
          f"comes before {sorted_arts[1]['name']} "
          f"({sorted_arts[1]['power']} power)")

    print("\nTesting spell transformer...")
    transformed = spell_transformer(spells)
    print(f"{transformed}")
    for spell in transformed:
        print(f"{spell}", end="  ")

    print("\n\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"{mages}")
    print(f"Stats: {stats}")
