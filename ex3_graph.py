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
								
					
	def isPath(self,firstNode,targetNode):
		"""Function to check if there is a path between two nodes.
		Similar to depth first search algorithm,
		travels the graph and if node has path
		prints the path to a txt file"""
		
		path = False
		stack = [] # list as a stack
		visited = []
		stack.append(firstNode)
		while stack != []:
			popped = stack.pop()
			if popped not in visited:
				visited.append(popped)
				if popped == targetNode: # if this is the targetnode
					path = True	# then there is a path
					break
				for neighbour in self.graph[popped]:
					stack.append(neighbour)
		f = open("ex3_isPath.txt","w")
		if path:
			f.write("The path is: " + str(visited))
			f.close()
		else:
			f.write("No path between two nodes.")
				
				
				


					
	
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


g.isPath(1,4)

print(g)