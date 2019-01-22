import json


def decode_characters(obj):
    if '__type__' in obj:
        elf = Elf(obj['name'], obj['level'], obj['ability_scores'])
        return elf
    else:
        return obj


class CharacterEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Elf):
            return {
                'name': obj.name,
                'level': obj.level,
                'ability_scores': obj.ability_scores,
                'hp': obj.hp,
                '__type__': 'elf'
            }
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)


class Elf:
    def __init__(self, name, level, ability_scores=None):
        self.name = name
        self.level = level
        self.ability_scores = {
            "str": 11, "dex": 12, "con": 10,
            "int": 16, "wis": 14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]