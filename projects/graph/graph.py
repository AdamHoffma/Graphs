"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("The vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty cue
        # Add the starting vertex ID to cue
        # Create an empty set to store visited nodes
        # While the cue is not empty
            # DeCue the first vertex
            # Check if it's been visited
            # If not visited
                # Mark as visited
                # Add all neighbors the the back of the cue

        cue = Queue()
        visited = set()
        cue.enqueue(starting_vertex)
        while cue.size() > 0:
            v = cue.dequeue()
            if v not in visited:
                print("BFT", v)
                visited.add(v)
                for neighbor  in self.get_neighbors(v):
                    cue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = Stack()
        visited = set()
        stack.push(starting_vertex)
        while stack.size() > 0:
            v = stack.pop()
            if v not in visited:
                print("DFT", v)
                visited.add(v)
                for neighbor in self.get_neighbors(v):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Check if the node is visited
        # If not
        #  HINT:  https://docs.python-guide.org/writing/gotchas/ 
            # mark it visited
            #Print
            #Call DFT_recursive on each child
        if visited is None:
            visited = set()
        visited.add(starting_vertex)
        print("DFT_RECURSIVE", starting_vertex)

        for next_vertex in self.vertices[starting_vertex]:
            if next_vertex not in visited:
                self.dft_recursive(next_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty cue
        # add a PATH to the starting vertex_id to the cue
        # create an empty set to store visited nodes
        # create an empty set
        # While cue is > 0
            # decue the first PATH
            # GRAB LAST VERTEX FROM THE PATH
            # Check if it is Target
                # If so return the PATH
            # check if it's been visited
            # if not in visited
                # Mark it visited
                # Add a PATH to all neighbors to the back of cue
                 # Make copy of the path before adding
        cue = Queue()
        cue.enqueue([starting_vertex])
        visited = set()
        while cue.size() > 0:
            path = cue.dequeue()
            last_vertex = path[-1]
            if last_vertex not in visited:
                if last_vertex == destination_vertex:
                    return path
                visited.add(last_vertex)
                for next in self.vertices[last_vertex]:
                    new_path = list(path)
                    new_path.append(next)
                    cue.enqueue(new_path)
            


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push([starting_vertex])
        visited = set()
        while stack.size() > 0:
            path = stack.pop()
            last_vertex = path[-1]
            if last_vertex == destination_vertex:
                return path
            visited.add(last_vertex)
            for next_node in self.vertices[last_vertex]:
                new_path = list(path)
                new_path.append(next_node)
                stack.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        for child_vert in self.vertices[starting_vertex]:
            if child_vert not in visited:
                new_path = self.dfs_recursive(child_vert, destination_vertex, visited, path)
                if new_path:
                    return new_path
        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    # '''
    # Should print:
    #     {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    # '''
    print(graph.vertices)

    # '''
    # Valid BFT paths:
    #     1, 2, 3, 4, 5, 6, 7
    #     1, 2, 3, 4, 5, 7, 6
    #     1, 2, 3, 4, 6, 7, 5
    #     1, 2, 3, 4, 6, 5, 7
    #     1, 2, 3, 4, 7, 6, 5
    #     1, 2, 3, 4, 7, 5, 6
    #     1, 2, 4, 3, 5, 6, 7
    #     1, 2, 4, 3, 5, 7, 6
    #     1, 2, 4, 3, 6, 7, 5
    #     1, 2, 4, 3, 6, 5, 7
    #     1, 2, 4, 3, 7, 6, 5
    #     1, 2, 4, 3, 7, 5, 6
    # '''
    graph.bft(1)

    # '''
    # Valid DFT paths:
    #     1, 2, 3, 5, 4, 6, 7
    #     1, 2, 3, 5, 4, 7, 6
    #     1, 2, 4, 7, 6, 3, 5
    #     1, 2, 4, 6, 3, 5, 7
    # '''
    graph.dft(1)
    graph.dft_recursive(1)

    # '''
    # Valid BFS path:
    #     [1, 2, 4, 6]
    # '''
    print("BFS", graph.bfs(1, 6))

    # '''
    # Valid DFS paths:
    #     [1, 2, 4, 6]
    #     [1, 2, 4, 7, 6]
    # '''
    print("DFS", graph.dfs(1, 6))
    print("DFS_RECURSIVE", graph.dfs_recursive(1, 6))
