while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letter and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Passworks can only have letters and numbers.')