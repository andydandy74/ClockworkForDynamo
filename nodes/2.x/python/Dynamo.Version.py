import clr
from System.Reflection import Assembly
from System.Diagnostics import Process
dynamoCore = Assembly.Load("DynamoCore")
version_long = dynamoCore.GetName().Version.ToString()
version_short = version_long[:5]
proc = Process.GetCurrentProcess().ProcessName
OUT = (version_short,version_long,proc)