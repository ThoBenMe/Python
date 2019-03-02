""" This little program shows the use of the enumerate() - operator """

def enuming():
	t = [6, 7, 8, 19, 42]
	for p in enumerate(t)
		print(p)


def enuming2():
	x = [192, 135, 643, 346]
	for i, v in enumerate(x):
		print("i = {}, v = {}".format(i,v))

		
""" range() isn't used widely in python!:
>>> list(range(0,10,2))
>>> [0, 2, 4, 6, 8]
"""