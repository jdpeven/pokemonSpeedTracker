# Remove comments
# cat pokedex.txt | grep "[^\"]:"


class PokemonList:
    _all_pokemon: list
    _input_file: str

    def __init__(self, input_file: str):
        self._input_file = input_file
        self._load_file(input_file)

    def _load_file(self, file_name: str) -> None:
        with open(file_name, "r") as f:
            self._parse_data(f.readlines())

    def _parse_data(self, lines: list) -> None:
