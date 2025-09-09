class Game:
    name = ""
    yearlaunch = 0
    multiplayer = False
    note = 0
    
# Primrio jogo
game1 = Game()
game1.name = "The legend of zelda: Breath of the wild"
game1.yearlaunch = 2017
game1.multiplayer = False
game1.note = 9.5

# Segundo jogo
game2= Game()
game2.name = "Fortnite"
game2.yearlaunch = 2017
game2.multiplayer = True
game2.note = 8.5

# Terceiro Jogo

# Quarto Jogo

print("## Dados do Jogo ##")
print(f"Nome do jogo: {game1.name}\nAno de Lançamento: {game1.yearlaunch}")
print(f"\nNome do jogo: {game2.name}\nAno de Lançamento: {game2.yearlaunch}")