class Graph(object):
	"""Class for unweighted undirected graph
	where key is a vertex
	and values are neighbouring vertices"""
	
	def __init__(self):
		"""Instantiation method,
		initializes graph as a dictionary"""
			
		self.graph = {}
		
	def add_vertex(self,vertex):
		"""Adding a vertex
		as a key in dictionary"""
		
		if vertex not in self.graph:
			self.graph[vertex] = []
		else:
			print("No duplicate vertices allowed")
			
	def add_edge(self,firstVertex,secondVertex):
		"""Adding an edge
		first vertex is key and second is value
		and vice-versa
		to connect vertices in a graph"""
		
		self.graph[firstVertex].append(secondVertex)
		self.graph[secondVertex].append(firstVertex)
			
	def __repr__(self):
		"""returns the graph"""
		
		return str(self.graph)
								
					
	def isConnected(self):
		"""Function to check if the graph is connected.
		Graph is connected when there is a path between every pair of vertices.
		Similar to depth first search algorithm,
		travels the graph and if it is connected
		prints Yes. Otherwise prints No."""
		
		stack = []
		visited = []
		start = list(self.graph.keys())[0] # start point of traversal
		stack.append(start)
		while stack != []:
			popped = stack.pop()
			if popped not in visited:
				visited.append(popped)
				for neighbour in self.graph[popped]:
					stack.append(neighbour)
		if len(visited) != len(self.graph.keys()): # if number of visited keys not equal to number of total keys
			print("No")
		else:
			print("Yes")


					
	
g = Graph()

g.add_vertex(1)
g.add_vertex(2)
g.add_vertex(3)
g.add_vertex(4)
g.add_vertex(5)
g.add_vertex(6)

g.add_edge(1,2)
g.add_edge(3,1)
g.add_edge(4,2)
g.add_edge(5,3)
g.add_edge(4,3)


print(g)
g.isConnected()