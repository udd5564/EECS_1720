
from random import *

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} made unit".format(name))

    def move(self, location):
        print("[Ground Unit Move]")
        print("{0} : Move to {1} direction. [Speed {2}]"\
            .format(self.name, location, self.speed))
    
    def damaged(self, damage):
        print("{0} : {1} got a damage.".format(self.name, damage))
        self.hp -= damage
        print("{0} : The current strength {1}.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : Destroyed.".format(self.name))

class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0}: Attacke to {1} direction.  [attack {2}]"\
            .format(self.name, location, self.damage))

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "Marine", 40, 1, 5)

    def stimpack(self):
        if self.hp> 10:
            self.hp -= 10
            print("{0}: used stimpack. (HP 10 dcreased.)".format(self.name))
        else:
            print("{0} : It doesn't have enough hp. It dosen't use stimpack.".format(self.name))

class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "tank", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        
        if self.seize_mode == False:
            print("{0} : Turn on the Seize mode".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : Turn off the Seize mode".format(self.name))
            self.damage /= 2
            self.seize_mode = False
        

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : Fly to {1} direction. [speed {2}]"\
            .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) 
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("[Moving the flayable unit]")
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "Wraith", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} : Turn off the clocking mode.".format(self.name))
            self.clocked = False
        else:
            print("{0} : Turn on the clocking mode.".format(self.name))
            self.clocked = True

def game_start():
    print("[Notice] Start new game!")

def game_over():
    print("Player : gg")
    print("[Player] has left.")

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine() 

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1pm")

Tank.seize_developed = True
print("[NOTICE] Success developed Tank seize mode.")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit,Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1pm")

for unit in attack_units:
    unit.damaged(randint(5, 21))

game_over()