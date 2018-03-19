spam = ['apples', 'bananas', 'tofu', 'cats', 'birds']

# example from https://stackoverflow.com/questions/38824634/automate-the-boring-stuff-with-python-comma-code
# def commaCode(someList):
#     if len(someList) == 1:
#         return someList[0]
#     return '{}, and {}'.format(', '.join(someList[:-1]), someList[-1])

def commaCode(someList):
    list = ''                               # creates a blank list to build on
    for i in spam:                          # creates variable i to loop through spam list
        maxLen = len(spam)                  # creates variable to set length of spam list
        if spam.index(i) != (maxLen -1):    # i increments by 1 per loop, this checks to see if i is set to less than -1
            list = list + i + ', '          # modifies list to include i as it increments through each loop
        else:
            list = list + 'and ' + i        # once the if statement reaches -1, list is set to add 'and' before last i
    print(list)                             # print list that will now include 'and' before the last item in the list


commaCode(spam)                             # runs commaCode function using the spam list
