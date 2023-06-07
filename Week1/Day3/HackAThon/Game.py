from rpg_classes.player import Player
from rpg_classes.warrior import Warrior


Xeno = Player('Xeno')
Cloud = Player('Cloud')
Xeno.Attack(Cloud)

Tryndamere = Warrior('Tryndamere')
Tryndamere.Enrage().WildSwing(Xeno).Enrage().WildSwing(Xeno).Defend(Xeno.attack)


favorite_color = input('What is your favorite color? ') # input takes a prompt, which needs to be a string
print(f'Your favorite color is: {favorite_color}') #output, prints the color given to the console
