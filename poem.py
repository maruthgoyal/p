from random import choice
import sys
from word import word
stdin = sys.stdin

flatten = lambda l: [item for sublist in l for item in sublist]
word_sets = [[[y.upper() for y in x.split()] + ['\n'] for x in poem.split('<br />')] for poem in stdin.read().splitlines()]
dic = {None:word(None)}
for poem in word_sets:
	for line in poem:
		line = [None] + line
		for w in xrange(len(line) - 1):
			if line[w] not in dic:
				dic[line[w]] = word(line[w])
			
			if line[w+1] not in dic:
				dic[line[w+1]] = word(line[w+1])

			dic[line[w]].increment_edge(dic[line[w+1]])
n = dic[None]
while True:
	if n.edges is None:
		n = choice(flatten([x[0] for y in xrange(x[1])] for x in dic[None].edges.values()))
	else:
		n = choice(flatten([x[0] for y in xrange(x[1])] for x in n.edges.values()))
	print n.w,