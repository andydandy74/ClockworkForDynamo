import clr
import re
groups = {}
guids = []
names = []
datatypes = []
datacategories = []
groupnames = []
visible = []
description = []
usermodifiable = []
for line in IN[0].splitlines():
	line = re.split(r'\t', line)
	if line[0] == "GROUP":
		groups[line[1]] = line[2]
	if line[0] == "PARAM":
		guids.append(line[1])
		names.append(line[2])
		datatypes.append(line[3])
		datacategories.append(line[4])
		groupnames.append(groups[line[5]])
		visible.append(line[6] == "1")
		description.append(line[7])
		usermodifiable.append(line[8] == "1")
OUT = names, guids, datatypes, datacategories, groupnames, description, visible, usermodifiable