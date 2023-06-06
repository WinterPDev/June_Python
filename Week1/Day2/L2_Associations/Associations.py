'''
-----------------------------------
Types of methods in Python:

Instance Methods - Accessed via named instances of an object.
Class Methods - Accessed via the class name or object name. Can affect class attributes that are shared among all objects of that class.
Static Methods - Accessed via the class name or object name. Utility functions that do not modify or access the class/instances. 
-----------------------------------

Associating Classes with Objects!

Associating classes is as simple as accessing another object's attributes or methods through a different class.


'''

class Player:

    Game_Name = 'Lost Frontier'
    Player_List = []

    def __init__(self, name, hp, attack, defense, abilities, companion):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.abilities = abilities
        self.companion = companion
        Player.Player_List.append(self)

    def PlayerInfo(self):
        print(f'Player Name : {self.name}\n HP: {self.hp}\n Attack: {self.attack}\n Defense : {self.defense} \n Abilities : {self.abilities}')

    def TakeDamage(self, dmg):
        self.hp = self.hp - (dmg - self.defense)
        print(f'Player {self.name} takes {dmg - self.defense}! \n Current HP : {self.hp}')

    @classmethod
    def GetAllPlayers(cls):
        for player in cls.Player_List:
            print(f'Player Name : {player.name}\n HP: {player.hp}\n Attack: {player.attack}\n Defense : {player.defense} \n Abilities : {player.abilities}')

class Companion:

    def __init__(self, name, abilities, mana=100) -> None:
        self.name = name
        self.abilities = abilities
        self.mana = mana

    # PetAttack Parameters:
    # self = The Companion that is performing the attack
    # target = the Player the Companion is attacking
    def PetAttack(self, target):
        self.mana -= 10
        print(f'{self.name} used {self.abilities[0]}, it cost 10 Mana.')
        target.hp = target.hp - (10 - target.defense)
        print(f'{self.name} Damaged {target.name} for {10 - target.defense} !')
# Objective 1: Complete the class method to list all players.

# Objective 2: Create a Companion class with Attributes that include name, mana, and abilities to make a companion for our Players.


Agumon = Companion('Agumon', ['Pepper Breath'])
Onyx = Companion('Onyx', ['Rock Smash'])

Xeno = Player('Xeno', 100, 10, 5, ['Slash', 'Fireball', 'Waterga'], Agumon)
Toph = Player('Toph', 120, 20, 1, ['Rock Sling', 'Blindsight', 'Metalbending'],Onyx)


# Xeno.PlayerInfo()
# Player.GetAllPlayers()

# print(Agumon.name)
print(Xeno.companion.name)

Xeno.companion.PetAttack(Toph)

# Objective 3: Store the current Companion they have into an attribute of the Player, that way we can access their information as well as their methods.

# Objective 4: Give the companion a heal spell that can replenish HP of a target at the cost of mana
