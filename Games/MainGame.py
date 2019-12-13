#from Live import CallGame
from Games import Games
G = Games()
if G.chosen_game == 2:
    G.check_answer()
elif G.chosen_game == 1:
