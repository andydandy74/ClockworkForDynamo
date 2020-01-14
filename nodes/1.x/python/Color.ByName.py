import clr
clr.AddReference('System.Drawing')
import System.Drawing

def ColorByName(str):
	syscol = System.Drawing.Color.FromName(str)
	return syscol.R,syscol.G,syscol.B
	

if isinstance(IN[0], list): OUT = map(list, zip(*[ColorByName(x) for x in IN[0]]))
else: OUT = ColorByName(IN[0])