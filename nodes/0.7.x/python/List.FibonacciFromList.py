fibseq = IN[0]
iterations = IN[1]
counter = 0
while counter < iterations:
	fibseq.append(fibseq[len(fibseq)-2] + fibseq[len(fibseq)-1])
	counter += 1
OUT = fibseq