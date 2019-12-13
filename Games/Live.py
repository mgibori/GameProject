class CallGame:
    def __init__(self, name):

        self.name = name
        self.name = self.name.capitalize()
        self.welcome_message = self.welcome()
        self.chosen_game = self.choose_game
        self.game_dif = self.choose_difficulty()

    def welcome(self):
        name = self.name.capitalize()
        print('Hello {Name} and welcome to the world of games \nHere you can find many cool games to play'.format(Name=name))

    @property
    def choose_game(self):
        print("Please choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you "
              "have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer\n3. "
              "Currency Roulette - try and guess the value of a random amount of USD in ILS")
        game_choice = int(input(self.name+', which game would you like to play? (1-3)'))
        while True:
            if 1 <= game_choice <= 3:
                break
            else:
                game_choice = int(input(self.name+', which game would you like to play?\nPlease choose a number between 1-3:'))
        return game_choice

    def choose_difficulty(self):    
        game_difficulty = int(input(self.name+', Please choose game difficulty from 1 to 5:'))
        while True:
            if 1 <= game_difficulty <= 5:
                break
            else:
                game_difficulty = int(input(self.name+', choose a difficulty, a number between 1-5:'))
        return game_difficulty
