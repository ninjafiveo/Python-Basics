#enemy class
class enemy:
    boss_name =  ""
    hitpoints = 0 
    luck = 0
    attack_damage = 0
    defense = 0
    reward_points = 0
    
    def __init__(self, name, hitpoints, luck, attack_damage, defense, reward_points):
        self.boss_name = name
        self.hitpoints = hitpoints
        self.luck = luck
        self.attack_damage = attack_damage
        self.defense = defense
        self.reward_points = reward_points
    
    def enemy_attack(self, player):
        pass
    def enemy_defense(self, player):
        pass


class player:
    player_name =  ""
    hitpoints = 0 
    luck = 0
    attack_damage = 0
    defense = 0
    gold = 0
    
    def play_attack(self, enemy):
        pass
    def player_defense(self, enemy):
        pass

blob_the_builder = enemy("Blob the Builder", 100, 3, 10, 3, 100)
kaitlyn_the_torturer =  enemy("Kaitlyn the Torturer", 300, 10, 50, 10, 500)

print(f"{kaitlyn_the_torturer.boss_name} attacks for {kaitlyn_the_torturer.attack_damage}.")
kaitlyn_the_torturer.attack_damage = kaitlyn_the_torturer.attack_damage * 1.5

print(f"{kaitlyn_the_torturer.boss_name} get's 150% increase in damage and attacks again for {kaitlyn_the_torturer.attack_damage}.")
