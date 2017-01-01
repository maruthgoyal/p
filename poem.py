from random import choice
import sys
from word import word
stdin = sys.stdin

flatten = lambda l: [item for sublist in l for item in sublist]

word_sets = [[[y.upper() for y in x.split()] + ['\n'] for x in poem.split('<br />')] for poem in stdin.read().splitlines() if poem != '<br />']
word_sets = [flatten(x) for x in word_sets]

dic = {None:word(None)}

for poem in word_sets:
	poem = [None] + poem
	for w in xrange(len(poem) - 1):
		if poem[w] not in dic:
			dic[poem[w]] = word(poem[w])
		
		if poem[w+1] not in dic:
			dic[poem[w+1]] = word(poem[w+1])

		dic[poem[w]].increment_edge(dic[poem[w+1]])
n = dic[None]
while True:
	if n.edges is None:
		n = dic[None]
	
	n = choice(flatten([x[0] for y in xrange(x[1])] for x in n.edges.values()))
	print n.w,