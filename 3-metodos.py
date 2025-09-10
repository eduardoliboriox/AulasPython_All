class Game:
    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0):
        self.name = name
        self.yearlaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note   

    def __str__(self):
        return f"Game: {self.name}"
    
game1 = Game("The legend of zelda", 2017, False, 9.5)
game2 = Game("Resident Evil", 2018, True, 7.5)
 

print("## Dados do Jogo ##")
print(f"Nome do jogo: {game1.name}\nAno de Lançamento: {game1.yearlaunch}")
print(f"\nNome do jogo: {game2.name}\nAno de Lançamento: {game2.yearlaunch}")


