import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import Clipboard
try:
	Clipboard.SetText(IN[0])
	OUT = IN[0]
except:
	OUT = 'Data could not be copied to clipboard'