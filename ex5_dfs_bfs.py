
class Graph(object):
	def __init__(self):
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
								
					
	def depth_first_search(self,startNode):
		stack = []
		visited = []
		stack.append(startNode)
		while stack != []:
			popped = stack.pop()
			if popped not in visited:
				visited.append(popped)
				try:
					for neighbour in self.graph[popped]:
						stack.append(neighbour)
				except KeyError:
						print("The specified node does not exists in the graph!")
						print("Cannot perform depth first search.")
						visited = None
		f = open("dfs_bfs.txt","w")
		f.write("This is the dfs path: " + str(visited) + "\n")
		f.close()
		
	def breadth_first_search(self,startNode):
		queue = []
		visited = []
		queue.append(startNode)
		while queue != []:
			popped = queue.pop(0)
			if popped not in visited:
				visited.append(popped)
				try:
					for neighbour in self.graph[popped]:
						queue.append(neighbour)
				except KeyError:
						print("The specified node does not exists in the graph!")
						print("Cannot perform breadth first search.")
						visited = None
		f = open("dfs_bfs.txt","a")
		f.write("This is the bfs path: " + str(visited))
		f.close()


					
	
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
g.depth_first_search(1)
g.breadth_first_search(1)