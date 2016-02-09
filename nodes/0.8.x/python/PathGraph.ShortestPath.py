pathgraphlist = IN[0]
start = IN[1]
end = IN[2]
pathgraph = dict()

for item in pathgraphlist:
	pathgraph[item[0]] = item[1]

# script found here:
# https://www.python.org/doc/essays/graphs/

def find_shortest_path(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return path
	if not graph.has_key(start):
		return None
	shortest = None
	for node in graph[start]:
		if node not in path:
			newpath = find_shortest_path(graph, node, end, path)
			if newpath:
				if not shortest or len(newpath) < len(shortest):
					shortest = newpath
	return shortest

OUT = find_shortest_path(pathgraph,start,end)