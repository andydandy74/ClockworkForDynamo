import clr
import sys
pyt_path = r'C:\Program Files (x86)\IronPython 2.7\Lib'
sys.path.append(pyt_path)
import xml.etree.ElementTree as ET
import json

class CustomNode:
	def __init__(self):
		self.Version = None
		self.Name = None
		self.ID = None
		self.Description = None
		self.Category = None
		self.VisibleInLibrary = True
		self.Inputs = []
		self.InputDescriptions = []
		self.InputDataTypes = []
		self.InputDefaultValues = []
		self.Outputs = []
		self.OutputDescriptions = []
		self.PythonScripts = []
		self.NestedCustomNodes = []
		self.CustomNodesCount = []
		self.NestedBuiltinNodes = []
		self.BuiltinNodesCount = []		
	def ByJSON(self, str):
		data = json.loads(str)
		self.Version = data['View']['Dynamo']['Version']
		self.Name = data['Name']
		self.ID = data['Uuid']
		self.Description = data['Description']
		self.Category = data['Category']
		self.VisibleInLibrary = data['View']['Dynamo']['IsVisibleInDynamoLibrary']
		for node in data['Nodes']:
			if node['NodeType'] == "InputNode":
				self.Inputs.append(node['Parameter']['Name'])
				self.InputDescriptions.append(node['Parameter']['Description'].strip())
				self.InputDataTypes.append(node['Parameter']['TypeName'])
				if node['Parameter']['DefaultValue']: self.InputDefaultValues.append(node['Parameter']['DefaultValue'])
				else: self.InputDefaultValues.append('')
			elif node['NodeType'] == "OutputNode":
				outputdef = node['Symbol'].split('\r\n')
				self.Outputs.append(outputdef[-1])
				outputdef2 = ''
				if len(outputdef) > 1: 
					for line in outputdef[:-1]: outputdef2 += line[2:].strip() + " "
				self.OutputDescriptions.append(outputdef2)
			elif node['NodeType'] == 'PythonScriptNode': self.PythonScripts.append(node['Code'])
			elif node['NodeType'] == 'FunctionNode' and node['Concrete'+'Type'] == 'Dynamo.Graph.Nodes.CustomNodes.Function, DynamoCore':
				customnodename = data['View']['NodeViews'][data['Nodes'].index(node)]['Name']
				if customnodename not in self.NestedCustomNodes:
					self.NestedCustomNodes.append(data['View']['NodeViews'][data['Nodes'].index(node)]['Name'])
					self.CustomNodesCount.append(1)
				else: self.CustomNodesCount[self.NestedCustomNodes.index(customnodename)] += 1
			else:
				builtinnodename = data['View']['NodeViews'][data['Nodes'].index(node)]['Name']
				if builtinnodename not in self.NestedBuiltinNodes:
					self.NestedBuiltinNodes.append(data['View']['NodeViews'][data['Nodes'].index(node)]['Name'])
					self.BuiltinNodesCount.append(1)
				else: self.BuiltinNodesCount[self.NestedBuiltinNodes.index(builtinnodename)] += 1			
	def ByXML(self, str):
		root = ET.fromstring(str)
		self.Version = root.get("Version")
		self.Name = root.get("Name")
		self.ID = root.get("ID")
		self.Description = root.get("Description")
		self.Category = root.get("Category")
		isvisible = root.get("IsVisibleInDynamoLibrary")
		if isvisible: self.VisibleInLibrary = isvisible		
		for child in root:
			if child.tag == "Elements":
				for element in child:
					if element.tag == "Dynamo.Nodes.Symbol" or element.tag == "Dynamo.Graph.Nodes.CustomNodes.Symbol":
						for symbol in element:
							inputdef = symbol.get("value")
							inputdef2 = inputdef.split(":")
							if inputdef2[0].startswith('//'):
								inputdef4 = inputdef2[0].splitlines()
								self.Inputs.append(inputdef4[-1].strip())
								self.InputDescriptions.append(inputdef4[0][2:].strip())
							else:
								self.Inputs.append(inputdef2[0].strip())
								self.InputDescriptions.append("")
							if len(inputdef2) > 1:
								inputdef3 = inputdef2[1].split("=")
								self.InputDataTypes.append(inputdef3[0].strip())
								if len(inputdef3) > 1: self.InputDefaultValues.append(inputdef3[1].strip())
								else: self.InputDefaultValues.append("")
							else:
								self.InputDataTypes.append("")
								self.InputDefaultValues.append("")
					elif element.tag == "Dynamo.Nodes.Output" or element.tag == "Dynamo.Graph.Nodes.CustomNodes.Output":
						for symbol in element:
							outputdef = symbol.get("value")
							if outputdef != None:
								if outputdef.startswith('//'):
									outputdef2 = outputdef.splitlines()
									self.Outputs.append(outputdef2[-1].strip())
									self.OutputDescriptions.append(outputdef2[0][2:].strip())
								else:
									self.Outputs.append(outputdef.strip())
									self.OutputDescriptions.append("")
					elif element.tag == "DSIronPythonNode.PythonNode" or element.tag == "PythonNodeModels.PythonNode":
						for script in element:
							if script.text != None: self.PythonScripts.append(script.text)
					elif element.tag == "Dynamo.Nodes.Function" or element.tag == "Dynamo.Graph.Nodes.CustomNodes.Function":
						if element.get("nickname") in self.NestedCustomNodes:
							self.CustomNodesCount[self.NestedCustomNodes.index(element.get("nickname"))] += 1
						else:
							self.NestedCustomNodes.append(element.get("nickname"))
							self.CustomNodesCount.append(1)
					else:
						if element.get("nickname") in self.NestedBuiltinNodes:
							self.BuiltinNodesCount[self.NestedBuiltinNodes.index(element.get("nickname"))] += 1
						else:
							self.NestedBuiltinNodes.append(element.get("nickname"))
							self.BuiltinNodesCount.append(1)

def CustomNodeByFormat(str):
	CN = CustomNode()
	if str.startswith("<Workspace"): CN.ByXML(str)
	else: CN.ByJSON(str)
	return (CN.Version, CN.Name, CN.ID, CN.Description, CN.Category, CN.Inputs, CN.InputDataTypes, CN.InputDefaultValues, CN.Outputs, CN.PythonScripts, CN.NestedCustomNodes, CN.CustomNodesCount, CN.NestedBuiltinNodes, CN.BuiltinNodesCount, CN.InputDescriptions, CN.OutputDescriptions, CN.VisibleInLibrary)

if isinstance(IN[0], list): OUT = map(list, zip(*[CustomNodeByFormat(x) for x in IN[0]]))
else: OUT = CustomNodeByFormat(IN[0])