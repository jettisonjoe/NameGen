# NameGen - A set of utities for randomly generating various types
# of names. Started as a tool for generating abstract project names.

import random

f = open("oed.txt")
WORDLIST = f.readlines()
f.close()

def n_random_words(n):
	result = []
	while len(result) < n:
		# The top (0th) line of oed.txt is purposely skipped.
		k = random.randint(1, len(WORDLIST))
		line = WORDLIST[k]
		if len(line) > 3:
			result.append(WORDLIST[k])
	return result


def random_vlamb_style():
	result = []
	while len(result) < 1:
		line = n_random_words(1)[0]
		if ' adj. ' in line: result.append(line)
	while len(result) < 2:
		line = n_random_words(1)[0]
		if ' n. ' in line: result.append(line)
	return result



def main():
	random.seed()

	#print '\n'.join(n_random_words(2))
	print '\n'.join(random_vlamb_style())


if __name__ == "__main__":
	main()