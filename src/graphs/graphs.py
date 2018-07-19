#graphs are used to represent systems
#vertex: node that has a payload
#edge connects two vertices to show a relationship
#digraph or directed graph: all edges are one way
#weight: show some other parameter or cost associated with one edge

graph = { "a" : ["c"],
          "b" : ["c", "e"],
          "c" : ["a", "b", "d", "e"],
          "d" : ["c"],
          "e" : ["c", "b"],
          "f" : []
        } 

print(graph)
def find_path(graph, start, end, path = []):
	path = path + [start]
	if start == end:
		return path
	for node in graph[start]:
		if node not in path:
			newpath = find_path(graph,node,end,path)
			if newpath:
				return newpath
	return None
	
print(find_path(graph, 'a', 'e'))
	
    

