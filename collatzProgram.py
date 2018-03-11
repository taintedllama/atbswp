def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        print(3 * number + 1)
        return 3 * number + 1

try:
    print('Enter a number:')
    n = input()
    while n != 1:
        n = collatz(int(n))
except ValueError:
    print('Number must be in integer.')