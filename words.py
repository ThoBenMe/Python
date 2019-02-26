import sys
from urllib.request import urlopen

def fetch_words(url):
	with urlopen(url) as story:
		story_words = []
		for line in story:
			line_words = line.decode('utf-8').split()
			for word in line_words:
				story_words.append(word)
	return story_words
	

def print_items(items):
	for item in items:
		print(item)
		
		
def main(url):
	words = fetch_words(url)
	print_items(words)
	
	
if __name__ == '__main__':
	main(sys.argv[1])
	

""" Start code by typing into REPL: main("http://........") """

""" Former Code -> moved into the main()
if __name__ == '__main__':
		words = fetch_words()
		print_items(words)
		"""

""" Import data in REPL with: from words import fetch_words
		OR:
		import words
		words.fetch_words() 
		"""
		
""" To use the double underscore statement:
	python words.py <-- this will ask the program, if the modules name matches the importet main
	(which is the case) and then executes the fetch_words() function 
	OR: 
	__name__ is a buildt-in variable which returns the modules name.
	"""

""" def fetch_words():
	with urlopen('http://sixty-north.com/c/t.txt') as story: <-- is also an old code fragment """

	