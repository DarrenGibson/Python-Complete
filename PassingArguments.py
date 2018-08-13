#---------------------------------------------------------------------
#                       Passing Arguments
#---------------------------------------------------------------------

'''
Date:       08/13/18
Author:     Darren / andrew Reese - stack overflow
Subject:    function arguments
Resources:  https://stackoverflow.com/questions/51806150/difficulty-understanding-return-values-and-function-parameters-in-python
'''

'''
# my version
def getInfo():

    a = int(input('Please enter the first number in the range:'))
    b = int(input('Please enter the second number in the range:'))
    return a, b

def loopIt(a, b):

    for i in range(a, b):
        print('i is now {}'.format(i))

getInfo()
loopIt(a, b)
'''



# correct version

def getInfo():
    a = int(input('Please enter a number: '))
    b = int(input('Please enter a number'))
    return a, b
def loopIt(data):
    a, b = data
    for i in range(a, b):
        print('i is now {}'.format(i))

loopIt(getInfo())










































