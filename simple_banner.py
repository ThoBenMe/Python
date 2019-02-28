def banner(message, border='*'):	# defining a function which takes the actual message and the symbols printed as the border as a parameter
	""" prints a banner by having the same amount of symbols as letters in the message. """
	line = len(message) * border	# symbols will appear as much as there are letters in the message
	print(line)
	print(message)
	print(line)
