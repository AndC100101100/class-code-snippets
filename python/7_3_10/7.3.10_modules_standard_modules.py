import sys
import math

if len(sys.argv) != 2:
    print("enter a number and ill square it")
    sys.exit("Example: \npython 7.3.10_modules_standard_moodules.py 200")

number = sys.argv[1]
print(math.sqrt(int(number)))
