import clr

keys1 = IN[0]
keys2 = IN[2]
items1 = IN[1]
items2 = IN[3]
exclude = IN[4]

unified, keys_done = [],[]
for i in range(len(keys1)):
	for j in range(len(keys2)):
		if keys1[i] == keys2[j]:
			unified.append((keys1[i],items1[i],items2[j]))
			keys_done.append(keys1[i])
	if keys1[i] not in keys_done and not exclude:
		unified.append((keys1[i],items1[i],[]))
		keys_done.append(keys1[i])
for k in range(len(keys2)):
	if keys2[k] not in keys_done and not exclude:
		unified.append((keys2[k],[],items2[k]))
		keys_done.append(keys2[k])
OUT = unified