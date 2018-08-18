import clr
clr.AddReference("System.Management")
from System.Management import ManagementObject, ManagementObjectSearcher
sysinfo = ManagementObjectSearcher("Select NumberOfProcessors, NumberOfLogicalProcessors from Win32_ComputerSystem").Get()
for sysdata in sysinfo:
	physicalProcessors = sysdata.Item["NumberOfProcessors"]
	logicalProcessors = sysdata.Item["NumberOfLogicalProcessors"]
sysinfo = ManagementObjectSearcher("Select NumberOfCores, MaxClockSpeed from Win32_Processor").Get()
cores = 0
for sysdata in sysinfo:
	cores += sysdata.Item["NumberOfCores"]
	cpuspeed = sysdata.Item["MaxClockSpeed"]
OUT = (physicalProcessors, logicalProcessors, cores, float(cpuspeed)/1000)