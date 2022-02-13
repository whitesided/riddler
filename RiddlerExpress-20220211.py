#!/usr/bin/env python3

#How high a sum will we check? Build out our list
topTrapezoidal = 10000
trapezoidals = []
for index in range(0,topTrapezoidal+1):
	trapezoidals.append([])

#Let's not check the length of our list multiple times
cap = topTrapezoidal
for index in range(1,int(cap/2)):
	vals  = [str(x) for x in range(index,index+100)]
	sums = []
	for pos in range(1,len(vals)):
		sums.append(sum([int(x) for x in vals[0:pos+1]]))
	for sumIndex, aSum in enumerate(sums,2):
		if aSum < cap:
			stringVal = "+".join(vals[0:sumIndex])
			trapezoidals[aSum].append(stringVal)

trapezoidalsFound = []
for theSum, traps in enumerate(trapezoidals):
	trapLen = len(traps)
	if trapLen in trapezoidalsFound:
		continue
	else:
		trapezoidalsFound.append(trapLen)
		print('%5d'%theSum, '(%d):\n\t'%len(traps), '\n\t'.join(traps))
