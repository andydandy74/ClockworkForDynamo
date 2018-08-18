import clr

lists = IN[0]
sortindex = int(IN[1])
caseinsensitive = IN[2]
sortdescending = IN[3]

# make sure that case-insensitive is turned of if it is not strings we're sorting
if caseinsensitive == True and isinstance(lists[0][sortindex], basestring) == False:
	caseinsensitive = False
if caseinsensitive == True:
	if sortdescending == True:
		OUT = sorted(lists, key=lambda lists:lists[sortindex].lower(), reverse=True)
	else:
		OUT = sorted(lists, key=lambda lists:lists[sortindex].lower())
else:
	if sortdescending == True:
		OUT = sorted(lists, key=lambda lists:lists[sortindex], reverse=True)
	else:
		OUT = sorted(lists, key=lambda lists:lists[sortindex])