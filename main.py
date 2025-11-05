from army_inventory.Soldier import Soldier
from army_inventory.Weapon import Weapon
from army_inventory.Unit import Unit

w1 = Weapon("gun",35)
w2 = Weapon("rocet",35)
w3 = Weapon("tanks",35)

s1 =Soldier("avi","8200","compyuter")
s2 =Soldier("David","8200","compyuter")
s3 =Soldier("Mose","8200","compyuter")

u1 = Unit("8200",s1,[s2,s3])






