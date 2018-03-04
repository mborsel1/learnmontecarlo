import random
import matplotlib
import matplotlib.pyplot as plt
import time

sampleSize = 10000

startingFunds = 10000
wagerSize = 100
wagerCount = 100

def rollDice():
	roll = random.randint(1,100)
	
	if roll == 100:
		return False
	elif roll <= 50:
		return False
	elif 100 > roll > 50:
		return True
		
def double_bettor(funds, initial_wager, wager_count, color):
	global doubler_busts
	global doubler_profits
	
	value = funds
	wager = initial_wager
	wX = []
	vY = []
	currentWager = 1
	previousWager = "win"
	previousWagerAmount = initial_wager
	
	while currentWager <= wager_count:
		if previousWager == "win":
			if rollDice():
				value += wager
				wX.append(currentWager)
				vY.append(value)
			else:
				value -= wager
				previousWager = "loss"
				previousWagerAmount = wager
				wX.append(currentWager)
				vY.append(value)
				if value <= 0:
					doubler_busts += 1
					break
		elif previousWager == "loss":
			if rollDice():
				wager = previousWagerAmount * 2
				if (value - wager) < 0:
					wager = value
				value += wager
				wager = initial_wager
				previousWager = "win"
				wX.append(currentWager)
				vY.append(value)
			else:
				wager = previousWagerAmount * 2
				if (value - wager) < 0:
					wager = value
				value -= wager
				previousWager = "loss"
				previousWagerAmount = wager
				wX.append(currentWager)
				vY.append(value)
				if value <= 0:
					doubler_busts += 1
					break
		
		currentWager += 1
	
	plt.plot(wX, vY, color)
	if value > funds:
		doubler_profits += 1
	
def simple_bettor(funds, initial_wager, wager_count, color):
	global simple_busts
	global simple_profits
	
	value = funds
	wager = initial_wager 
	wX = []
	vY = []
	currentWager = 1
	while currentWager <= wager_count:
		if rollDice():
			value += wager
			wX.append(currentWager)
			vY.append(value)
		else:
			value -= wager
			wX.append(currentWager)
			vY.append(value)
			
			if value <= 0:
				simple_busts += 1
				break
		currentWager += 1
		
	plt.plot(wX, vY, color)
	if value > funds:
		simple_profits += 1
	
x = 0

simple_busts = 0.0
doubler_busts = 0.0

simple_profits = 0.0
doubler_profits = 0.0

while x < sampleSize:
	simple_bettor(startingFunds, wagerSize, wagerCount, 'c')
	#simple_bettor(startingFunds, wagerSize*2, wagerCount, 'c')
	double_bettor(startingFunds, wagerSize, wagerCount, 'k')
	x += 1

print "Simple Bettor Bust Chances: ", ((simple_busts/sampleSize)*100.00)
print "Double Bettor Bust Chances: ", ((doubler_busts/sampleSize)*100.00)

print "Simple Bettor Profit Chances: ", ((simple_profits/sampleSize)*100.00)
print "Double Bettor Profit Chances: ", ((doubler_profits/sampleSize)*100.00)
	
	
plt.axhline(0, color = 'r')
plt.ylabel('Account Value')
plt.xlabel('Wager Count')
plt.show()
