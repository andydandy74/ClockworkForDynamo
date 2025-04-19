if isinstance(IN[0], list): OUT = [bin(x)[2:] for x in IN[0]]
else: OUT = bin(IN[0])[2:]