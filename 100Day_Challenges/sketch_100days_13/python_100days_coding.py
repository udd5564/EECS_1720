from random import *
users = range(1,21)
users = list(users)
shuffle(users)

winners = sample(users, 4) 
print("-- the winners --")
print("Winners for chicken : {0}".format(winners[0]))
print("Winners for coffee : {0}".format(winners[1:]))
print("-- Congratulation -- ")