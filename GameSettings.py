from pokemon import Pokemon
from pokemonList import PokemonList


class GameSettings:
    _pokemon_list: PokemonList
    rounds = 0
    score = 0
    _difficulty = 0

    def __init__(self, pokemon_list: PokemonList):
        self._pokemon_list = pokemon_list
        self._difficulty = self._get_difficulty()

    def _get_difficulty(self):
        print("Select difficulty:")
        print("1) Easy - Speed +/- 50")
        print("2) Medium - Speed +/- 25")
        print("3) Hard - Speed +/- 10")
        while True:
            val = input()
            if val == "1":
                return 1
            if val == "2":
                return 2
            if val == "3":
                return 3
            print("Please enter 1, 2, or 3")

    def play_basic_game(self):
        base_pokemon = self._get_random_poke()
        while True:
            second_pokemon = self._get_random_poke_with_difficulty(
                base_pokemon=base_pokemon, difficulty=self._difficulty)

            self._print_prompt(base_pokemon, second_pokemon)
            val = self._read_input()
            if val == 8:
                self._difficulty = self._get_difficulty()
            if val == 9:
                break
            self._evaluate_results(base_pokemon, second_pokemon, val)
            self.rounds += 1
            base_pokemon = second_pokemon

    def _print_prompt(self, base_pokemon: Pokemon, second_pokemon: Pokemon):
        print("Rounds: {0}. Score: {1}. Difficulty: {2}".format(self.rounds, self.score, self._difficulty))
        print("Which is faster?")
        print("1: #{0} {1}".format(base_pokemon.get_dex_num(), base_pokemon.get_name()))
        print("2: #{0} {1}".format(second_pokemon.get_dex_num(), second_pokemon.get_name()))
        print("3: Equal")
        print("8: Change difficulty")
        print("9: Quit")

    def _read_input(self) -> 1:
        while True:
            val = input()
            if val == "1":
                return 1
            if val == "2":
                return 2
            if val == "3":
                return 3
            if val == "8":
                return 8
            if val == "9":
                return 9
            print("Please enter 1, 2, 3, 8, or 9")

    def _evaluate_results(self, base_pokemon: Pokemon, second_pokemon: Pokemon, val: int):
        if base_pokemon.get_speed() > second_pokemon.get_speed():
            if val == 1:
                print("Correct! {0}({1}) is faster than {2}({3}).".format(
                    base_pokemon.get_name(),
                    base_pokemon.get_speed(),
                    second_pokemon.get_name(),
                    second_pokemon.get_speed()))
                self.score += 1
            else:
                print("Incorrect! {0}({1}) is faster than {2}({3}).".format(
                    base_pokemon.get_name(),
                    base_pokemon.get_speed(),
                    second_pokemon.get_name(),
                    second_pokemon.get_speed()))
            return
        if base_pokemon.get_speed() < second_pokemon.get_speed():
            if val == 2:
                print("Correct! {0}({1}) is faster than {2}({3}).".format(
                    second_pokemon.get_name(),
                    second_pokemon.get_speed(),
                    base_pokemon.get_name(),
                    base_pokemon.get_speed()))
                self.score += 1
            else:
                print("Incorrect! {0}({1}) is faster than {2}({3}).".format(
                    second_pokemon.get_name(),
                    second_pokemon.get_speed(),
                    base_pokemon.get_name(),
                    base_pokemon.get_speed()))
        if base_pokemon.get_speed() == second_pokemon.get_speed():
            if val == 3:
                print("Correct! {0}({1}) is equal to {2}({3}).".format(
                    second_pokemon.get_name(),
                    second_pokemon.get_speed(),
                    base_pokemon.get_name(),
                    base_pokemon.get_speed()))
                self.score += 1
            else:
                print("Incorrect! {0}({1}) is equal to {2}({3}).".format(
                    second_pokemon.get_name(),
                    second_pokemon.get_speed(),
                    base_pokemon.get_name(),
                    base_pokemon.get_speed()))

    def _get_random_poke(self) -> Pokemon:
        return self._pokemon_list.get_random_pokemon()

    def _get_speed_range(self, difficulty: int):
        if difficulty == 1:
            return 50
        if difficulty == 2:
            return 25
        if difficulty == 3:
            return 10

    def _get_random_poke_with_difficulty(self, base_pokemon: Pokemon, difficulty: int) -> Pokemon:
        speed_range = self._get_speed_range(difficulty)
        return self._pokemon_list.get_random_pokemon_within_range(base_pokemon, speed_range)
