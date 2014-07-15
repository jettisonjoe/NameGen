# NameGen - A set of utities for randomly generating various types
# of names. Started as a tool for generating abstract project names.

import random

PARTS_OF_SPEECH = [ 'v',
					'n',
					'adj',
					'adv' ]

f = open("oed.txt")
WORDLIST = f.readlines()
f.close()

def random_entry():
	result = ''
	while result is '':
		k = random.randint(1, len(WORDLIST))
		line = WORDLIST[k]
		if len(line) > 3:
			result = line
	return result

def n_random_words(n):
	result = []
	while len(result) < n:
			result.append(random_entry())
	return result

def random_of_type(s):
	assert s in PARTS_OF_SPEECH
	result = ''
	while result is '':
		entry = random_entry()
		if (s+'.') in entry:
			result = entry
	return result

def random_v_style():
	result = []
	result.append(random_of_type('adj'))
	result.append(random_of_type('n'))
	return result

def main():
	random.seed()

	#print '\n'.join(n_random_words(2))
	#print '\n'.join(random_vlamb_style())
	#print random_entry()
	print '\n'.join(random_v_style())


if __name__ == "__main__":
	main()