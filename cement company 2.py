acceptedCement = []
acceptedSand = []
acceptedGravel = []

totalC = []
totalS = []
totalG = []
print()
while True:
	# For Cement
	c = input("Enter weight of Cement Sack: ") #could do "inputs" with "try" and "except" to stop 
													#errors but ...
	if c.lower() == 'q':
		break
	elif int(c) > 43.5 and int(c) < 49.7:
		acceptedCement.append(c)
	totalC.append(c)

#for Sand
	s = input("Enter weight of Sand Sack: ")
	if s.lower() == 'q':
		break
	if int(s) > 22.9 and int(s) < 33.2:
		acceptedSand.append(c)
	totalS.append(s)
#For Gravel
	g = input("Enter weight of Gravel Sack: ")
	if g.lower() == 'q':
		break
	if int(g) > 22.9 and int(g) < 33.2:
		acceptedGravel.append(c)	
	totalG.append(g)
	
print()
print(f"Total accpeted Cement sacks are: {len(totalC) - len(acceptedCement)}")
print(f"Total accpeted Sand sacks are: {len(totalS) - len(acceptedSand)}")
print(f"Total accpeted Gravel sacks are: {len(totalG) - len(acceptedGravel)}")

