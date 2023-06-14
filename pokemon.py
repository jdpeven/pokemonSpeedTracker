
class PokemonStats:
    _hp: int
    _atk: int
    _defense: int
    _spa: int
    _spd: int
    _spe: int
    _bst: int

    def __init__(self, hp: int, atk: int, defense: int, spa: int, spd: int, spe: int):
        self._hp = hp
        self._atk = atk
        self._defense = defense
        self._spa = spa
        self._spd = spd
        self._spe = spe
        self._bst = self._hp + self._atk + self._defense + self._spa + self._spd + self._spe

    def __str__(self):
        return "hp: {0}, atk: {1}, def: {2}, spa: {3}, spd: {4}, spe: {5}, bst: {6}".format(
            self._hp, self._atk, self._defense, self._spa, self._spd, self._spe, self._bst)

    def get_bst(self):
        return

    def get_hp(self):
        return self._hp

    def get_atk(self):
        return self._atk

    def get_def(self):
        return self._defense

    def get_spa(self):
        return self._spa

    def get_spd(self):
        return self._spd

    def get_spe(self):
        return self._spe


class Pokemon:
    _name: str
    _dex_num: int
    _pokemon_stats: PokemonStats

    def __init__(self, name, dex_num, stats: dict):
        self._name = name
        self._dex_num = dex_num
        self._stats = PokemonStats(
            hp=stats["hp"],
            atk=stats["atk"],
            defense=stats["def"],
            spa=stats["spa"],
            spd=stats["spd"],
            spe=stats["spe"])

    def __str__(self):
        return "{0}, #{1}, stats: {2}".format(self._name, self._dex_num, self._stats)

    def get_name(self):
        return self._name

    def get_dex_num(self):
        return self._dex_num

    def get_speed(self):
        return self._stats.get_spe()



