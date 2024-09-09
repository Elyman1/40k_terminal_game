class Attack:
    def __init__(self, name: str, attack_type: str, num_attacks: int, 
                 attack_strength: int, damage: int):
        self.name = name
        self.attack_type = attack_type
        self.num_attacks = num_attacks
        self.attack_strength = attack_strength
        self.damage = damage

    def perform(self, attacker, target):
        target.take_damage(self.damage)

    def roll_hit(self):
        import random
        dice_roll = random.randint(1, 1)
        return dice_roll <= self.hit_chance
    
    def take_buff(self, buff_amount, attribute):
        pass
    
    def take_debuff(self, debuff_amount):
        pass



        