from random import choice
import sys
from word import word
from fractions import Fraction

stdin = sys.stdin


def gcd(x, y):
   """This function implements the Euclidian algorithm
   to find G.C.D. of two numbers"""

   while(y):
       x, y = y, x % y

   return x

# define lcm function
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   lcm = (x*y)//gcd(x,y)
   return lcm

def lcm_seq(s):
	return reduce(lcm, s)


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

del word_sets

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

for b in xrange(10):
	
	if n.edges is None:
		n = dic[None]

	l = lcm_seq(x[0].prob[n.w].denominator for x in n.edges.values())
	l = lcm(l, p.denominator)
	
	new_n = choice(flatten([x[0] for y in xrange(((p.numerator * (l/p.denominator)) * (x[0].prob[n.w].numerator * (l / x[0].prob[n.w].denominator))))] for x in n.edges.values()))
	
	print new_n.w,

	if p < 0.00001:
		p = 1
	else:
		p *= new_n.prob[n.w]

	n = new_n

