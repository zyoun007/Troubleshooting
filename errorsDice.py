import random



rolls = int(input ('How many times do you want to roll?'))
sides = int(input ('How many sides is your die?'))


for rolls in range (rolls):
    randomDice = random.randrange (sides)+1
    print (randomDice)
    if sides==20:
        if randomDice ==20:
            print ('Critical Hit')
    if sides==1: 
        if randomDice==1:
            print ('Critical Fail')
    

