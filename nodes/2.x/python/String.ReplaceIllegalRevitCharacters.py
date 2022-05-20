def ReplaceIllegalRevitChars(str, repl):
	str = str.replace('\\', repl)
	str = str.replace(':', repl)
	str = str.replace('{', repl)
	str = str.replace('}', repl)
	str = str.replace('[', repl)
	str = str.replace(']', repl)
	str = str.replace('|', repl)
	str = str.replace(';', repl)
	str = str.replace('<', repl)
	str = str.replace('>', repl)
	str = str.replace('?', repl)
	str = str.replace('`', repl)
	str = str.replace('~', repl)
	return str

strings = IN[0]

if isinstance(IN[0], list): OUT = [ReplaceIllegalRevitChars(x, IN[1]) for x in strings]
else: OUT = ReplaceIllegalRevitChars(strings, IN[1])