from math import ceil
class word(object):

	def __init__(self, w):

		self.w = w
		self.edges = None
		self.prob = {}
	

	def increment_edge(self, n, x):

		if self.edges is None:
			self.edges = {}

		if n.w in self.edges:
			self.edges[n.w][1] += x
		else:
			self.edges[n.w] = [n,x]

		self.edges[n.w][1] = min(self.edges[n.w][1] % 20, self.edges[n.w][1])
