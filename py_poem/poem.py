from __future__ import print_function
from random import choice
from random import randint
import sys
from word import word
import pymongo
import re
import pronouncing as ps
from math import ceil

#stdin = sys.stdin

flatten = lambda l: [item for sublist in l for item in sublist]

PERCENT = 0.05
# word_sets = [[[y.upper() for y in x.split()] + ['\n'] for x in poem.split('<br />')] for poem in stdin.read().splitlines() if poem != '<br />']
# word_sets = [flatten(x) for x in word_sets]

dic = {None:word(None)}

connection = pymongo.MongoClient('mongodb://localhost:27017')
db = connection['poems']
col = db['poem_collection']

for poem in col.find():
	#print poem['title']
	poem = re.split(r'(\s+)', poem['poem'])
	poem = filter(lambda x: x != ' ', poem)
	poem = [None] + poem

	for x in poem:
		if x not in dic:
			dic[x] = word(x)

	for w in xrange(len(poem) - 1):
		
		dic[poem[w]].increment_edge(dic[poem[w+1]], 1.0)

		l = set(ps.rhymes(poem[w]))

		for x in poem:
			if x in l:
				val = dic[poem[w]].edges[x][1] if x in dic[poem[w]].edges else 1
				dic[poem[w]].increment_edge(dic[x], PERCENT * val)

def getnextword(n):
	x = randint(0, sum(int(ceil(a[1])) for a in n.edges.values()) - 1)
	for y in n.edges.values():
		x -= int(ceil(y[1]))
		if x <= 0:
			return y[0]

n = dic[None]
while True:
	if n.edges is None:
		n = dic[None]

	n = getnextword(n)
	print(n.w, end=' ')
