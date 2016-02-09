pathgraphlist = IN[0]
start = IN[1]
end = IN[2]
pathgraph = dict()

for item in pathgraphlist:
	pathgraph[item[0]] = item[1]

# script found here:
# https://www.python.org/doc/essays/graphs/

def find_all_paths(graph, start, end, path=[]):
	path = path + [start]
	if start == end:
		return [path]
	if not graph.has_key(start):
		return []
	paths = []
	for node in graph[start]:
		if node not in path:
			newpaths = find_all_paths(graph, node, end, path)
			for newpath in newpaths:
				paths.append(newpath)
	return paths

OUT = find_all_paths(pathgraph,start,end)