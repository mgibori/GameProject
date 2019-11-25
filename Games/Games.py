from Live import CallGame
b = CallGame("aaa")
class Games():
    def __init__(self, user_guess):
        self.user_guess = user_guess
        self.secret_number = self.generate_number()

    def generate_number(self):
        import random
        secret_number = random.randint(1, self)
        return secret_number

    def check_answer(self):
        if self.user_guess == self.secret_number:
            answer = "Woohoo, you got it right"
        else:
            answer = "Wrong, Try Again"
        print(answer)

Games



