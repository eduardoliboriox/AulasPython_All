class Game:
    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0):
        self.name = name
        self.yearlaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note  
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
        
    def avarage(self):
        print(f"Média do jogo {self.name}: {self.totalEvalution / self.evalutors}")
        
game1 = Game("The legend of zelda", 2017, False, 9.5)
game2 = Game("Resident Evil", 2018, True, 7.5)
 
game1.technical_sheeet()
game2.technical_sheeet()
game1.evaluate(9.0)
game1.evaluate(7.5)
game1.avarage()



