import random
def rockpaperscissors():
    print "Welcome to rock paper scissors"
    print "What is your move?"
    answer = raw_input("Type r, p or s OR R, P or S and hit 'Enter':")
    if answer == "r" or answer == "R" or answer == "p" or answer =="P" or answer == "s" or answer == "S":
        print "This is a legal move."

	computerchoices = ['r','p','s']
	pcchoice = random.choice(computerchoices)
	print pcchoice



	rockpaperscissors()
    else:
        print "That's not fair. Tournament over"
        

rockpaperscissors()
