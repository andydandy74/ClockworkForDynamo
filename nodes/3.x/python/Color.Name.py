import clr
clr.AddReference('System.Drawing')
import System.Drawing

def GetColorName(color):
	if hasattr(color, "Red"):
		if color.Red == 0 and color.Green == 0 and color.Blue == 0: return "Black"
		else:
			lookup = [x for x in knowncols if x.R == color.Red and x.G == color.Green and x.B == color.Blue]
			if len(lookup) > 0: return lookup[0].Name
			else: return None
	else: return None

knowncols = [System.Drawing.Color.FromKnownColor(x) for x in System.Enum.GetValues(System.Drawing.KnownColor)]
if isinstance(IN[0], list): OUT = [GetColorName(x) for x in IN[0]]
else: OUT = GetColorName(IN[0])