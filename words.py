from urllib.request import urlopen

def fetch_words():
	with urlopen('http://sixty-north.com/c/t.txt') as story:
		story_words = []
		for line in story:
			line_words = line.decode('utf-8').split()
			for word in line_words:
				story_words.append(word)
				
	for word in story_words:
		print(word)
	

if __name__ == '__main__':
		fetch_words()
		

""" Import data in REPL with: from words import fetch_words
		OR:
		import words
		words.fetch_words() 
		"""
		
""" To use the double underscore statement:
	python words.py <-- this will ask the program, if the modules name matches the importet main
	(which is the case) and then executes the fetch_words() function """
		

	