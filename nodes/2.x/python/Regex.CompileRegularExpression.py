import clr
import re

regexstring = IN[0]
flags = IN[1]
# process flags
if flags == "1111":
	thisexp = re.compile(regexstring, re.IGNORECASE|re.LOCALE|re.DOTALL|re.MULTILINE)
elif flags == "1110":
	thisexp = re.compile(regexstring, re.IGNORECASE|re.LOCALE|re.DOTALL)
elif flags == "1101":
	thisexp = re.compile(regexstring, re.IGNORECASE|re.LOCALE|re.MULTILINE)
elif flags == "1100":
	thisexp = re.compile(regexstring, re.IGNORECASE|re.LOCALE)
elif flags == "1011":
	thisexp = re.compile(regexstring, re.IGNORECASE|re.DOTALL|re.MULTILINE)
elif flags == "1010":
	thisexp = re.compile(regexstring, re.IGNORECASE|re.DOTALL)
elif flags == "1001":
	thisexp = re.compile(regexstring, re.IGNORECASE|re.MULTILINE)
elif flags == "1000":
	thisexp = re.compile(regexstring, re.IGNORECASE)
elif flags == "0111":
	thisexp = re.compile(regexstring, re.LOCALE|re.DOTALL|re.MULTILINE)
elif flags == "0110":
	thisexp = re.compile(regexstring, re.LOCALE|re.DOTALL)
elif flags == "0101":
	thisexp = re.compile(regexstring, re.LOCALE|re.MULTILINE)
elif flags == "0100":
	thisexp = re.compile(regexstring, re.LOCALE)
elif flags == "0011":
	thisexp = re.compile(regexstring, re.DOTALL|re.MULTILINE)
elif flags == "0010":
	thisexp = re.compile(regexstring, re.DOTALL)
elif flags == "0001":
	thisexp = re.compile(regexstring, re.MULTILINE)
else:
	thisexp = re.compile(regexstring)
OUT = thisexp