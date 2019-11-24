from Live import CallGame
from Games import Games
b=CallGame("Moran")
print(b.chosen_game)
print(b.game_dif)
aa = Games(b.game_dif)
print(aa.secret_number)