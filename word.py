class word(object):

	def __init__(self, w):

		self.w = w
		self.edges = None
		self.prob = {}

	def increment_edge(self, n):

		if self.edges is None:
			self.edges = {}

		if n.w in self.edges:
			self.edges[n.w][1] += 1
		else:
			self.edges[n.w] = [n,1]
