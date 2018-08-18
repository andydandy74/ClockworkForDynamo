import clr
clr.AddReference("System.Management")
from System.Management import ManagementObject, ManagementObjectSearcher
from System.Diagnostics import Process
sysinfo = ManagementObjectSearcher("Select Capacity from Win32_PhysicalMemory").Get()
installedMem = 0
for sysdata in sysinfo:
	installedMem += sysdata.Item["Capacity"]
sysinfo = ManagementObjectSearcher("Select FreePhysicalMemory from Win32_OperatingSystem").Get()
for sysdata in sysinfo:
	freeMem = sysdata.Item["FreePhysicalMemory"]
procMem = Process.GetCurrentProcess().WorkingSet64
OUT = (float(installedMem)/1073741824, float(freeMem)/1048576, float(procMem)/1073741824)