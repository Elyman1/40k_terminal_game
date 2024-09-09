import logging
from random import randint

from classes.attack import Attack
from classes.faction import Faction
from classes.strategem import Strategem
from classes.exceptions import CustomException


class EpicHero:
    def __init__(self, name: str, faction: str, attacks: list,
                 wounds: int, toughness: int,
                 strategems: list, invulnerable_save: int, cp: int):
        
        self.name = name
        self.faction = faction
        self.attacks = attacks
        self.wounds = wounds
        self.toughness = toughness
        self.strategems = strategems
        self.invulnerable_save = invulnerable_save
        self.cp = cp


    def is_alive(self):
        return self.wounds > 0

    def use_attack(self, attack, target):
        attack.perform(self, target)
        
    def take_damage(self, damage):
        self.wounds -= damage

    def take_debuff(self, debuff):
        pass

    def use_strategem(self, strategem, target):
        strategem.activate()

    def gain_cp(self):
        if self.cp == 6:
            self.cp = 6
        else:
            self.cp += 1

    def determine_hit_roll_needed(self, target, attack):
            try:
                if not isinstance(target, EpicHero) or not isinstance(attack, Attack):
                    raise TypeError
                if attack.attack_strength >= target.toughness * 2:
                    return 2
                elif attack.attack_strength > target.toughness:
                    return 3
                elif attack.attack_strength == target.toughness:
                    return 4
                elif attack.attack_strength <= target.toughness // 2:
                    return 6
                elif attack.attack_strength < target.toughness:
                    return 5
                else:
                    raise Exception
            except TypeError:
                logging.error("Wrong argument type given to 'determine_hit_roll_' function")
            except Exception as e:
                print(f"An unexpected Error occurred: {e}")
                return f"An unexpected Error occurred: {e}"


    def roll_dice(self, num_dice):
        return [randint(1, 6) for _ in range(num_dice)]
        
