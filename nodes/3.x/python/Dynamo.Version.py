import clr
from System.Reflection import Assembly
from System.Diagnostics import Process
dynamoCore = Assembly.Load("DynamoCore")
version_long = dynamoCore.GetName().Version.ToString()
version_parts = version_long.split(".")
version_short = version_parts[0] + "." + version_parts[1] + "." + version_parts[2]
proc = Process.GetCurrentProcess().ProcessName
OUT = (version_short,version_long,proc)