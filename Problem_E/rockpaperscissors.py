import random
tally = []
def rockpaperscissors():
    print "What is your move?",
    answer = raw_input("Type r, p or s and hit 'Enter':")
    if answer == "r" or answer == "p" or answer == "s":
        

	computerchoices = ['r','p','s']
	pcchoice = random.choice(computerchoices)
	print pcchoice


	if answer == pcchoice:
		print "Draw"
		tally.append('d')
	elif (answer == 'r' and pcchoice == 'p') or \
             (answer == 'p' and pcchoice == 's') or \
	     (answer == 's' and pcchoice == 'r'):
		print "You wins"
		tally.append('w')
	else:
		print "Computer wins"
		tally.append('l')

	rockpaperscissors()

    else:
	print "That's not fair. Tournament over"
	numwins = tally.count('w')
	numlosses = tally.count('l')
	if numwins > numlosses:
		print "You win"
	elif numwins < numlosses:
		print "You lose!!!"
	else:
	print "We tie"
        
	print "you won {} times".format(tally.count('w'))
	print "you lost {} times".format(tally.count('l'))
	print "we drew {} times".format(tally.count('d'))
        
print "Welcome to rock paper scissors"
rockpaperscissors()
