import random

'''
we set a counter for the amount of attempts, and a have_match variable,
which will indicate if two random numbers match. we while loop and as 
long as have_match remains False the loop  will keep runing.
Once we have two matching numbers we set this var to True which makes
the next iteration have the condition not be met and exit
'''

attempts = 0
have_match = False

while have_match == False:
    guess_1 = random.randrange(1, 101)
    guess_2 = random.randrange(1, 101)

    print("Are %d and %d the same?" % (guess_1, guess_2))
    attempts += 1

    if (guess_1 == guess_2):
        print("\nYou got a match after %d attempts" % (attempts))
        have_match = True
