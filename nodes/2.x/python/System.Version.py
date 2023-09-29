import clr
from System import Environment, Version
OSnames = ["Windows XP","Windows Vista","Windows 7","Windows 8","Windows 8.1","Windows 10","Windows 11"]
OSversions = [Version(5,1,2505),Version(6,0,5112),Version(6,1,7600),Version(6,2,9200),Version(6,3,9200),Version(10,0,10240),Version(10,0,20000)]
# source: https://www.gaijin.at/en/lstwinver.php
# and https://stackoverflow.com/questions/69038560/detect-windows-11-with-net-framework-or-windows-api
for OSname, OSversion in zip(OSnames, OSversions):
	if Environment.OSVersion.Version.CompareTo(OSversion) >= 0:
		thisOS = OSname
OUT = (thisOS,Environment.OSVersion.Version.ToString(),Environment.OSVersion.ServicePack)