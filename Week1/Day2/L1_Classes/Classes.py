'''
Objects are like objects in real life. They are a series of things that share properties. 
Objects in code are made from classes, but are organized similar to a dictionary.

-----------------------------------

Objects exist in Python in a lot of existing things we've worked with. 
Such as why we can use some METHODS for certain things and not others.
For example: We can use .pop() on lists, but not on integers. Or that we can use .append() on lists and not dictionaries. 

This is an example of 'Encapsulation' which is one of the 'Four Pillars of OOP'. Which can be summarized as: 

Grouping our code together into objects and their appropriate methods for organization based on how we use those objects.

-----------------------------------
Types of methods in Python:

Instance Methods - Accessed via named instances of an object.
Class Methods - Accessed via the class name or object name. Can affect class attributes that are shared among all objects of that class.
Static Methods - Accessed via the class name or object name. Utility functions that do not modify or access the class/instances. 
-----------------------------------

'''

# Objective 1: Build a class that represents a player in an RPG.

class Player:

    Game_Name = 'Lost Frontier'
    Player_List = []
    # Name, Hitpoints, Attack, Defense, Abilities
    def __init__(self, name, hp, attack, defense, abilities): # Constructor Method, called when using Player()
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.abilities = abilities
        Player.Player_List.append(self)

    # Create an Instance Method for Attacking/Taking Damage as well as showing the player's info.
    def PlayerInfo(self): # self is an implicit parameter, that gives us access to the instance we're using the method on.
        print(f'Player Name : {self.name}\n HP: {self.hp}\n Attack: {self.attack}\n Defense : {self.defense} \n Abilities : {self.abilities}')

    def TakeDamage(self, dmg):
        # Instance method that takes damage and deducts it from the hitpoints.
        self.hp = self.hp - (dmg - self.defense)
        print(f'Player {self.name} takes {dmg - self.defense}! \n Current HP : {self.hp}')

    
    
Xeno = Player('Xeno', 100, 10, 5, ['Slash', 'Fireball', 'Waterga'])
Toph = Player('Toph', 120, 20, 1, ['Rock Sling', 'Blindsight', 'Metalbending'])
# print(Xeno) # <__main__.Player object at 0x0000029E12AEE950> this is how our computer sees this instance of a Player.
# print(Xeno.name)
# Objective 2: Build Instance Methods for printing the details of the character, taking damage, or healing.

# Xeno.PlayerInfo()
# Toph.PlayerInfo()

# Xeno.TakeDamage(Toph.attack)

# Objective 3: Add a class attribute to track all the existing characters that have been made and build a class method to print them out.

print(Player.Game_Name)
Xeno.Game_Name = 'Lost Frontier: Found Frontier'
print(Xeno.Game_Name)