print("https://pythonnumericalmethods.berkeley.edu/notebooks/chapter07.03-Inheritance-Encapsulation-and-Polymorphism.html")
print("--------------------------------------------------------------------------------------------------------------------")

class Player:
    def __init__(self, name, position):
        self._name = name 
        self._position = position  
        self._injured = False  

    def play(self):
        pass  

    def is_injured(self):
        return self._injured

class Striker(Player):
    def play(self):
        return f"{self._name} is a forward and scores goals!"

class Defender(Player):
    def play(self):
        return f"{self._name} is a defender and blocks shots!"

def interact_with_player(player):
    print(player.play())
    if player.is_injured():
        print(f"{player._name} is injured!")
    else:
        print(f"{player._name} is fit and ready to play in the pitch!")

striker = Striker("Messi", "Striker")
defender = Defender("Pique", "Center-back")

interact_with_player(striker)
interact_with_player(defender)
