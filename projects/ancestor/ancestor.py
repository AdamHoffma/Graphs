from util import Stack, Queue
from graph import Graph

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()    
    for pair in ancestors:
        graph.add_vertex(pair[0])    
        graph.add_vertex(pair[1])
    for pair in ancestors:    
        graph.add_edge(pair[1], pair[0])        
        print(graph.vertices)
    cue = Queue()
    cue.enqueue([starting_node])
    max_path = 1
    earliest_ancestor = -1
    while cue.size() > 0:
        path = cue.dequeue()        
        vertex = path[-1]
        if (len(path) >= max_path and vertex < earliest_ancestor) or (len(path) > max_path):
            earliest_ancestor = vertex
            max_path = len(path)            
        for neighbor in graph.vertices[vertex]:
            path_copy = list(path)
            path_copy.append(neighbor)
            cue.enqueue(path_copy)    
    return earliest_ancestor


earliest_ancestor(test_ancestors, 3)



    