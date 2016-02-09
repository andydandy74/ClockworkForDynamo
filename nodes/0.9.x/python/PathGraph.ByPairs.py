indices = IN[0]
flatlist = IN[1]
pathgraph = dict()

# script found here:
# https://www.python.org/doc/essays/graphs/

for index in indices:
	indexlist = list()
	for item in flatlist:
		if index == item[0]:
			indexlist.append(item[1])
	pathgraph[index] = indexlist	
# convert dictionary to list as Dynamo does not allow Python dictionaries
OUT = pathgraph.items()