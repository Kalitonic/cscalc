print("How much CS should you have at 10 mins?")
t = 10 # time aka 10 mins
m = 12 # number of minions every 1 min aka 12 minions by 1 min
c = (t / 1.5) #cannon minions calculation
#c = int(c) # convert to interger
# aka 1 extra minon every 3 waves
# so, total time divided by 1.5, which is how
# much time it takes for 3 waves
tot = (t * m + c) # calculate total minions at 10 mins
#tot = int(tot) #convert number of total minions to an interger
e = (1.5 * 12) + 1 # e is exception; minions don't spawn until 1.5mins
# meaning we must subtract nonexistent waves that are calculated,
# the first three waves until 1.5mins, plus 1 cannon minion

tot = tot - e #remove the exception from total
tot = int(tot) # turn to interger
print("Ideally,", tot)
print("Short of 100% CS,")
print("a good goal to shoot for is 70%")
s = tot * .70 #calculate 70% CS score
s = int(s) #turn to interger
print("Which would be:", s) #print

# Now we gather user input
print("How much CS do you have?", end = ' ') #asks for current CS
CS = int(input()) #current CS input into variable
print("Time?", end = ' ') #asks for current time
time = float(input()) #current time input into variable

c = time / 1.5 #change c aka cannon minion calculation to be accurate for current time.

btot = (time * m + c) #btot aka best total CS calculation for current time.
btot = btot - e #btot adjusted for first 1.5mins wout minions
missed = btot - CS # calculate missed by subtracting current CS with best total CS
ctot = btot - missed # calculate current CS total by subtracting best total with missed CS
percent = ctot / btot #divide ctot with btot for CS percentage
print(ctot, btot, percent) # checking accuracy of calculations
percent = percent * 100 # get into percentage form by multiplying by 100
percent = int(percent) # get int value to avoid .xxx format
print(f"You have {percent}% CS!") # print percentage!
