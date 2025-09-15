
class Game:
    total_games = 0 
    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0):
        self.name = name
        self.yearlaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note 
        Game.total_games += 1 
        self.evalutors = 0
        self.totalEvalution = 0 

    def __str__(self):
        return f"Game: {self.name}"
    
    def technical_sheeet(self):
        print("## Dados do Jogo ##")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de Lançamento: {self.yearlaunch}")
        print(f"Modo Multiplayer: {self.multiplayer}")
        print(f"Avaliação do jogo: {self.note}\n")
    
    def evaluate(self, note):
        self.totalEvalution += note
        self.evalutors += 1
        
    def average(self):
        print(f"Média do jogo {self.name}: {self.totalEvalution / self.evalutors}")
        
game1 = Game("The legend of zelda", 2017, False, 9.5)
game2 = Game("Resident Evil", 2018, True, 7.5)
game3 = Game("Silent Hill 4", 2014, True, 8.0)
 
game1.technical_sheeet()
game2.technical_sheeet()
game3.technical_sheeet()
game1.evaluate(9.0)
game1.evaluate(7.5)
game2.evaluate(6.5)
game2.evaluate(7.5)
game3.evaluate(8.4)
game3.evaluate(8.6)
game1.average()
game2.average()
game3.average()

# Exibindo o número total de jogos criados
print(f"Total de jogos criados: {Game.total_games}")



