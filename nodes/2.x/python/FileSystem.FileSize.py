import clr
import System.IO.FileInfo
files = IN[0]
bytes = []
kbytes = []
mbytes = []
for file in files:
	size = file.Length
	bytes.append(size)
	kbytes.append(float(size)/1024)
	mbytes.append(float(size)/1048576)
OUT = (bytes,kbytes,mbytes)