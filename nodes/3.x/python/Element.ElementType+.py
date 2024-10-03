def GetElementType(element):
	try: return element.Document.GetElement(element.GetTypeId())
	except: return None

items = UnwrapElement(IN[0])

if isinstance(IN[0], list): OUT = [GetElementType(x) for x in items]
else: OUT = GetElementType(items)