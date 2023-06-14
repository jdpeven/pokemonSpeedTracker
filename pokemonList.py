import json
import random

from pokemon import Pokemon

# Find ,\n[\t]*},\n
# Replace \n\t},\n


class PokemonList:
    _all_pokemon: list
    _input_file: str
    _speed_tiers: dict  # {tier: [pokemon]}

    def __init__(self, input_file: str = "./pokedex.txt"):
        self._input_file = input_file
        self._all_pokemon = []
        self._load_file(input_file)

    def _load_file(self, file_name: str) -> None:
        with open(file_name, "r") as f:
            self._parse_data(json.load(f))

    def _parse_data(self, data: dict) -> None:
        for name in data.keys():
            stats = data.get(name)
            if int(stats["num"]) > 0:
                self._all_pokemon.append(Pokemon(name, stats["num"], stats["baseStats"]))

        self._speed_tiers = {}
        for poke in self._all_pokemon:
            if self._speed_tiers.get(poke.get_speed(), None) is None:
                self._speed_tiers[poke.get_speed()] = [poke]
            else:
                self._speed_tiers[poke.get_speed()].append(poke)

    def _print_pokemon_list(self, pokemon: list):
        for p in pokemon:
            print(p)

    def print_all_pokemon(self):
        for pokemon in self._all_pokemon:
            print(pokemon)

    def get_random_pokemon_within_range(self, base_pokemon: Pokemon, speed_range: int):
        sub_list = []
        base_speed = base_pokemon.get_speed()
        min_speed = max(0, base_speed - speed_range)
        max_speed = min(200, base_speed + speed_range)
        for i in range(min_speed, max_speed):
            for p in self._speed_tiers.get(i, []):
                if base_pokemon.get_name() != p.get_name():
                    sub_list.append(p)
        return random.choice(sub_list)

    def print_speed_tiers(self):
        for k in self._speed_tiers.keys():
            print("{0}: {1}".format(k, self._print_pokemon_list(self._speed_tiers[k])))

    def get_pokemon_by_speed(self, spe: int) -> list:
        return self._speed_tiers.get(spe, [])

    def get_random_pokemon(self):
        return random.choice(self._all_pokemon)
