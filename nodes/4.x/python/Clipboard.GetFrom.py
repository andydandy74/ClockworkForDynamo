import clr
import System
from System.Threading import Thread, ThreadStart
clr.AddReference("System.Windows.Forms")

clipboardcontents = '###'

def GetText():
    def thread_proc():
        global clipboardcontents
        clipboardcontents = System.Windows.Forms.Clipboard.GetText()
    t = Thread(ThreadStart(thread_proc))
    t.ApartmentState = System.Threading.ApartmentState.STA
    t.Start()
    t.Join()

try:
	GetText()
	OUT = clipboardcontents
except:
	OUT = 'Data could not be copied to clipboard'