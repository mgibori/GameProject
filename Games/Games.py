from Live import CallGame
import time
import os
import random
from random import randint
cg = CallGame("aaa")


class Games():
    def __init__(self):
        self.difficulty = cg.game_dif
        self.chosen_game = cg.chosen_game
        # self.user_guess = int(input('Please take a guess\nchoose a number between 1-'+str(cg.game_dif)))
        self.secret_number = self.generate_number()
        self.memory_numbers = self.memory_numbers()

    def generate_number(self):
        secret_number = random.randint(1, self.difficulty)
        return secret_number

    def check_answer(self):
        user_guess = int(input('Please take a guess\nchoose a number between 1-'+str(cg.game_dif)))
        if self.secret_number == user_guess:
            answer = "Woohoo, you got it right"
        else:
            answer = "Wrong, better luck next time"
        print(answer)

    def memory_numbers(self):
        mem_numbers = [randint(0, 101) for i in range(0, self.difficulty)]
        return mem_numbers

    def check_mem_answer(self):
        print(self.memory_numbers)
        time.sleep(0.7)

        def clear():
            lambda: os.system('cls')
        clear()
        print('Please write the '+str(cg.game_dif)+' numbers displayed - one at a time')
        user_guess = list()
        for i in range(0, int(cg.game_dif)):
            num = int(input())
            user_guess.append(num)
        if self.memory_numbers == user_guess:
            answer = "Woohoo, you got it right"
        else:
            answer = "Wrong, better luck next time"
        print(answer)






