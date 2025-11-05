
class Weapon():

    total_weapons = 0

    def __init__(self,name,ammo):

        self.name = name
        self.ammo = ammo
        Weapon.total_weapons += 1


