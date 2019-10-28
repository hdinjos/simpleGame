class Hero:
    number = 0
    def __init__(self, inputName, inputHealth, inputAttack, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.attack = inputAttack
        self.armor = inputArmor
        Hero.number += 1
    def Attacking(self, Hero):
        print(self.name + " is Attacking " + Hero.name)
        Hero.Attacked(self, self.attack) #attack power Queeny

    def Attacked(self, Hero, attackPowerEnemie): #argument for attack power Queeny
        '''
        for get decrease health bar / HP enemy or 
        who were attaked 
        you must:
            get taking attack and cut down his(who were attaked) health bar,
            so, you will have last HP(after the cut down)
        for get a taking attack / attack force, 
        you must:
            devide Attack who is attaking by
        Defend/armor who were attaked 
        '''
        print(self.name + " Attacked by " + Hero.name)
        takingAttack = attackPowerEnemie / self.armor
        print("Attack Force is " + str(takingAttack))
        self.health -= takingAttack
        print("Health Point " + self.name + " still " + str(self.health))

queeny = Hero("Queeny", 100, 15, 10)
zerou = Hero("Zerou", 100, 20, 30)

zerou.Attacking(queeny) # can repeatly to HP become 0
print("\n")
zerou.Attacking(queeny)
print("\n")
zerou.Attacking(queeny)
print("\n")
zerou.Attacking(queeny)
print("\n")
zerou.Attacking(queeny)
print("\n")
zerou.Attacking(queeny)
print("\n")
zerou.Attacking(queeny)
print("\n")
