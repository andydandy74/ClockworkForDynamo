import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

refgroup = UnwrapElement(IN[0])
groups = UnwrapElement(IN[1])

# Get Mirrored state of first family instance in reference group instance
refGroupMembers = refgroup.GetMemberIds()
numMembers = len(refGroupMembers)
counter = 0
membernum = None
refGroupType = refgroup.GroupType.Id.IntegerValue
for member in refGroupMembers:
	elem = refgroup.Document.GetElement(member)
	if elem.GetType().ToString() == "Autodesk.Revit.DB.FamilyInstance":
		state = elem.Mirrored
		membernum = counter
		famtype = elem.GetTypeId().IntegerValue
		break
	counter += 1
	
# Default values for flags
refGroupIntact = True
noFamInsts = False
# Set a flag if the reference group contains no family instances
if membernum == None: noFamInsts = True
else:
	bools = []
	# Compare Mirrored state with corresponding members of other group instances
	for group in groups:
		# Get number of group members
		theseMembers = group.GetMemberIds()
		theseMembersNum = len(theseMembers)
		# Set a flag if any group instance has more members than the reference group instance
		# (only if both are of the same group type)
		if theseMembersNum > numMembers and refGroupType == group.GroupType.Id.IntegerValue:
			refGroupIntact = False
			break
		# Return null if group is of another group type
		elif refGroupType != group.GroupType.Id.IntegerValue: bools.append(None)
		# Return null for group instances with excluded members
		elif theseMembersNum < numMembers: bools.append(None)
		# Return null if family instance to compare if of a diffent type
		elif group.Document.GetElement(theseMembers[membernum]).GetTypeId().IntegerValue != famtype: bools.append(None)
		# Otherwise compare Mirrored state
		else: bools.append(group.Document.GetElement(theseMembers[membernum]).Mirrored != state)
			
# Return null for all groups if the first group has excluded members
# or if it does not contain any fanily instances
if not refGroupIntact or noFamInsts: bools = [None] * len(groups)
	
OUT = bools