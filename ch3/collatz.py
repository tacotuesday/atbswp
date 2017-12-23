# This function performs the Collatz sequence on a user-entered number.
def collatz(number):
    try:
        number = int(input('Enter number: '))
    except ValueError:
        print('Please input a number.')



    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        print(number)

collatz(1)      # For debugging purposes: comment out if the function is used in another script.
