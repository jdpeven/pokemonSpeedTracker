from GameSettings import GameSettings
from pokemonList import PokemonList

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pokemon_list: PokemonList = PokemonList()
    pokemon_game: GameSettings = GameSettings(pokemon_list)
    pokemon_game.play_basic_game()



    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
