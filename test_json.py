import json
from pathlib import Path
from typing import List

from characters import decode_characters, CharacterEncoder, Elf
from hamcrest import *


def read_characters_from_file() -> List[Elf]:
    characters_file = Path('./characters.json')
    with characters_file.open() as stream:
        characters = json.load(stream, object_hook=decode_characters)
    return characters


def test_end_to_end():
    legolas, tranduil, demon_hunter = read_characters_from_file()
    legolas.level += 2
    tranduil.level -= 1
    demon_hunter.level += 3
    demon_hunter.ability_scores['str'] += 3

    characters_file = Path('test/characters.json')

    with characters_file.open('w') as stream:
        json.dump([legolas, tranduil, demon_hunter], stream, cls=CharacterEncoder)

    values = json.load(characters_file.open())
    expected_values = json.load((Path('./characters.json').open()))

    for index, char in enumerate(values):
        assert_that(values[index], has_entries(expected_values[index]))


