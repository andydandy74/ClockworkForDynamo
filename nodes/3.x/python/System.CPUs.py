import clr
clr.AddReference("System.Management")
from System.Management import ManagementObject, ManagementObjectSearcher
sysinfo = ManagementObjectSearcher("Select NumberOfProcessors, NumberOfLogicalProcessors from Win32_ComputerSystem").Get()
for sysdata in sysinfo:
	physicalProcessors = sysdata.get_Item("NumberOfProcessors")
	logicalProcessors = sysdata.get_Item("NumberOfLogicalProcessors")
sysinfo = ManagementObjectSearcher("Select NumberOfCores, MaxClockSpeed from Win32_Processor").Get()
cores = 0
for sysdata in sysinfo:
	cores += sysdata.get_Item("NumberOfCores")
	cpuspeed = sysdata.get_Item("MaxClockSpeed")
OUT = (physicalProcessors, logicalProcessors, cores, float(cpuspeed)/1000)