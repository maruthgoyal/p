from random import choice
import sys
from word import word
from fractions import Fraction

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

# Creating Transition probabilities
# Prob is a dictionary mapping a word to the conditional probability
# of this word occuring given the word occured.
for w in dic:

	if dic[w].edges is not None:
		sum_of_wts = sum(x[1] for x in dic[w].edges.values())

		for x in dic[w].edges:
			dic[w].edges[x][0].prob[w] = Fraction(dic[w].edges[x][1], sum_of_wts)

n = dic[None]
p = Fraction(1)

while True:
	if n.edges is None:
		n = dic[None]

	new_n = choice(flatten([x[0] for y in xrange((p * x[0].prob[n.w]).numerator)] for x in n.edges.values()))
	print new_n.w,

	if p < Fraction(1,10**5):
		p = new_n.prob[n.w]
	else:
		p *= new_n.prob[n.w]

	n = new_n







