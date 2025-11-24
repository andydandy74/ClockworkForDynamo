def ReplaceIllegalFilenameChars(str, repl):
	str = str.replace('/', repl)
	str = str.replace('?', repl)
	str = str.replace('<', repl)
	str = str.replace('>', repl)
	str = str.replace('\\', repl)
	str = str.replace(':', repl)
	str = str.replace('*', repl)
	str = str.replace('|', repl)
	str = str.replace('"', repl)
	str = str.replace('^', repl)
	return str

strings = IN[0]

if isinstance(IN[0], list): OUT = [ReplaceIllegalFilenameChars(x, IN[1]) for x in strings]
else: OUT = ReplaceIllegalFilenameChars(strings, IN[1])