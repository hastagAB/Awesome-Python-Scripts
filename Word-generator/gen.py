def getDict(file):
	words = set()
	with open(file) as d:
		for w in d.read().split("\n"):
			words.add(w.lower())
	return words

def isEng(word):
	englishWords = getDict("dictionary.txt")
	if word in englishWords:
		return True
	return False

def permutations(xl, length = -1, res=[], output=[]):
	if xl == [] or len(res) == length:
		output.append(res)
		return
	for i in range(len(xl)):
		permutations(xl[:i] + xl[i + 1:], length, res + [xl[i]], output)
	return output


while True:
	found = set()
	letters = [i for i in input("Choose letters: ")]
	for sz in range(2, len(letters)+1):
		print("\nSize:", sz, "letters")
		for comb in permutations(letters, sz ,[], []):
			if isEng("".join(comb)) and not "".join(comb) in found:
				print("Found word:", "".join(comb))
				found.add("".join(comb))
	print()
	