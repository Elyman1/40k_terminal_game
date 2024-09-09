class Strategem:
    def __init__(self, target, name: str, description: str,
                  effect, cp_cost: int):
        self.target = target
        self.name = name
        self.description = description
        self.effect = effect
        self.cp_cost = cp_cost

    def activate(self, target):
        self.effect(target)

class BuffStrength(Strategem):
    def __init__(self, target, increase_amount: int):
        name = "Buff Strength"
        description = "Increase the user's strength by 1"
        cp_cost = 1

        def increase_strength(hero):
            hero.strength += increase_amount

        super().__init__(target, name, description, increase_strength,
                         cp_cost)