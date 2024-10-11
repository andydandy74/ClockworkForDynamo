import clr
import System.IO

def GetFileSize(file):
	if str(file.GetType()) == "System.IO.FileInfo":
		size = file.Length
		return size, float(size)/1024, float(size)/1048576
	else: return None, None, None

files = IN[0]

if isinstance(IN[0], list): OUT = map(list, zip(*[GetFileSize(x) for x in files]))
else: OUT = GetFileSize(files)