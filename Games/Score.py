# class Score():
#     def __init__(self):

#
#
#         def add_score(self):

f = open("score.txt", "a+")
f.close()
f = open("score.txt", "r")
import os
empty = os.stat("score.txt").st_size == 0
if empty == True:
    old_score = 0
else:
    old_score = int(f.read())
print(old_score)
f.close()
current_score = int(old_score) + 5
f = open("score.txt", "w")
f.write(str(current_score))

print(current_score)
f.close()
