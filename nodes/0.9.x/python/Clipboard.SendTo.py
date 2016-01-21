import clr
import System
from System.Threading import Thread, ThreadStart
clr.AddReference("System.Windows.Forms")

def SetText(text):
    def thread_proc():
        System.Windows.Forms.Clipboard.SetText(text)
    t = Thread(ThreadStart(thread_proc))
    t.ApartmentState = System.Threading.ApartmentState.STA
    t.Start()
    
try:
	SetText(IN[0])
	OUT = IN[0]
except:
	OUT = 'Data could not be copied to clipboard'