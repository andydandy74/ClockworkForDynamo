import clr
clr.AddReference('System.Drawing')
import System.Drawing

def GetColorName(color):
    if hasattr(color, "Red"):
        lookup = [x for x in syscols if (x[1] == color.Red and x[2] == color.Green and x[3] == color.Blue)]
        if len(lookup) > 0: return lookup[0][0]
        else: return None
    else: return None

syscols = []
syscols.append(("Black",0,0,0))
syscols.append(("White",255,255,255))
potentialcols = dir(System.Drawing.KnownColor)
for pc in potentialcols:
    c = System.Drawing.Color.FromName(pc)
    if c.R > 0 or c.G > 0 or c.B > 0: syscols.append((pc,c.R,c.G,c.B))
if isinstance(IN[0], list): OUT = [GetColorName(x) for x in IN[0]]
else: OUT = GetColorName(IN[0])