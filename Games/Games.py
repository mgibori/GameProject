class Games():
    def __init__(self, user_guess):
        self.user_guess = user_guess
        self.secret_number = self.generate_number()


    def generate_number(self):
        a = self.user_guess
        print(a)
        import random
        secret_number = random.randint(1, a)
        return secret_number

    def check_answer(self):
        times = 3
        while (times>0):
            if (self.user_guess == self.secret_number):
                answer = "Woohoo"
            else:
                times -=1
                
                print("You have "+times+" tries left")

    #Input User Guess

