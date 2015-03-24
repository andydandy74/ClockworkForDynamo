import clr
clr.AddReference('System.Windows.Forms')
from System.Windows.Forms import Clipboard
try:
	OUT = Clipboard.GetText()
except:
	OUT = 'Clipboard contents could not be retrieved'