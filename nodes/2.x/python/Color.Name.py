import clr
clr.AddReference('System.Drawing')
import System.Drawing

def GetColorName(color):
	if hasattr(color, "Red"):
		lookup = [x for x in syscols if x.R == color.Red and x.G == color.Green and x.B == color.Blue]
		if len(lookup) > 0: return lookup[0].Name
		else: return None
	else: return None

syscols = []
syscols.append(System.Drawing.Color.FromName("Black"))
syscols.append(System.Drawing.Color.FromName("White"))
syscols.extend([System.Drawing.Color.FromKnownColor(x) for x in System.Enum.GetValues(System.Drawing.KnownColor)])
if isinstance(IN[0], list): OUT = [GetColorName(x) for x in IN[0]]
else: OUT = GetColorName(IN[0])