import clr

def FileLastModified(file):
	if hasattr(file,"LastWriteTime"): return file.LastWriteTime
	else: return None

if isinstance(IN[0], list): OUT = [FileLastModified(x) for x in IN[0]]
else: OUT = FileLastModified(IN[0])