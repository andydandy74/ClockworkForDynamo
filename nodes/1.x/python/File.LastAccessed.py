import clr

def FileLastAccessed(file):
	if hasattr(file,"LastAccessTime"): return file.LastAccessTime
	else: return None

if isinstance(IN[0], list): OUT = [FileLastAccessed(x) for x in IN[0]]
else: OUT = FileLastAccessed(IN[0])