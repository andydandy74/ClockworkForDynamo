import clr

def FileCreated(file):
	if hasattr(file,"CreationTime"): return file.CreationTime
	else: return None

if isinstance(IN[0], list): OUT = [FileCreated(x) for x in IN[0]]
else: OUT = FileCreated(IN[0])