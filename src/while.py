'''
Created on 2011-4-22

@author: Administrator
'''
number = 33
run = True
while run:
    guess = int(raw_input("Please enter an Integer"))
    if guess == number:
        print "u got the correct number"
        run = False
    elif guess > number:
        print "ur guess is larger"
    else:
        print "ur guess is smaller"
else:
    print "loop ends"
