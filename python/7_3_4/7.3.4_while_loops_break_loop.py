import random

'''
we keep the while loops condition as True always and we add the break
statement in the case that our iteration reaches a point that we 
consider appropriate to exit the loop.
'''

attempts = 0
#have_match = False

while True:
    guess_1 = random.randrange(1, 101)
    guess_2 = random.randrange(1, 101)

    print("Are %d and %d the same?" % (guess_1, guess_2))
    attempts += 1

    if (guess_1 == guess_2):
        print("\nYou got a match after %d attempts" % (attempts))
        break
        print("This wont appear on your screen, we have exited")
