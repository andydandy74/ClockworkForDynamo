from System.IO import Directory, SearchOption
dir = IN[0]
searchstring = IN[1]
if Directory.Exists(dir):
	OUT = Directory.GetFiles(dir, searchstring, SearchOption.AllDirectories)
else:
	OUT = list()