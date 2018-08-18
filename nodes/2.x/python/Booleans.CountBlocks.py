import clr

booleans = IN[0]
truelist = list()
truelist.append(0)
truecounter = 0
falselist = list()
falselist.append(0)
falsecounter = 0

for item in booleans:
	if item == True:
		truelist[truecounter] += 1
		falsecounter += 1
		falselist.append(0)
	elif item == False:
		falselist[falsecounter] += 1
		truecounter += 1
		truelist.append(0)
OUT = (truelist,falselist)