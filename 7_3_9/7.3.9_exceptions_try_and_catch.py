print('Enter 2 numbers and I\'ll divide them')
print('Enter "q" to quit\n')

while True:
    first_input = input("First Number: ")
    if first_input == "q":
        break

    second_input = input("Second Number: ")
    if second_input == "q":
        break

    try:
        answer = int(first_input) / int(second_input)
    except ZeroDivisionError:
        print('Can\'t divide by zero, try again')
    except ValueError:
        print('Can\'t do words either, try again')
    else:
        print('Then answer is: ' + str(answer))
        print('Try Again')

print('Ciao')
