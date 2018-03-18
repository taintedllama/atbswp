spam = ['apples', 'bananas', 'tofu', 'cats', 'birds']

# This is an example from https://stackoverflow.com/questions/38824634/automate-the-boring-stuff-with-python-comma-code
# def commaCode(someList):
#     if len(someList) == 1:
#         return someList[0]
#     return '{}, and {}'.format(', '.join(someList[:-1]), someList[-1])

def commaCode(someList):
    list = ''                               # creates a black list to build on
    for i in spam:                          # starts the variable i to loop through spam list
        maxLen = len(spam)                  #
        if spam.index(i) != (maxLen -1):
            list = list + i + ', '
        else:
            list = list + 'and ' + i
    print(list)

commaCode(spam)