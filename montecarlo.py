import random

def rollDice():
	roll = random.randint(1,100)
	
	if roll == 100:
		#print roll, "roll was 100, you lose. What are the odds?! Play again!"
		return False
	elif roll <= 50:
		#print roll, "roll was between 1 and 50, you lose."
		return False
	elif 100 > roll > 50:
		#print roll, "roll was between 51 and 99, you win! *pretty lights flash* (play more!)"
		return True #true because user won
		
#x = 0

#while x < 100:
#	result = rollDice()
#	print result
#	x += 1
	
def simple_bettor(funds, initial_wager, wager_count):
	value = funds
	wager = initial_wager		

	currentWager = 0 #wager count

	while currentWager < wager_count:
		if rollDice():
			value += wager
		else:
			value -= wager
	
		currentWager += 1
	
	if value < 0:
		value = "You're broke!"
	print "Funds: ", value
			
x = 0

while x < 100:			
	simple_bettor(10000, 100, 10000)
	x += 1
	
	