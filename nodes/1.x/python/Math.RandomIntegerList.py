import clr
import System.Random

min = IN[0]
max = IN[1]
amount = IN[2]
seed = IN[3]

r = System.Random(seed)
randomInts = []
for i in range (0, amount):
	randomInts.append(r.Next(min, max+1))
OUT = randomInts