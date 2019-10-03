import random


# Custom Graph error
class GraphError(Exception): pass


class Graph:
    """
    Graph Class ADT
    """

    class Edge:
        """
        Class representing an Edge in the Graph
        """
        __slots__ = ['source', 'destination']

        def __init__(self, source, destination):
            """
            DO NOT EDIT THIS METHOD!
            Class representing an Edge in a graph
            :param source: Vertex where this edge originates
            :param destination: ID of Vertex where this edge ends
            """
            self.source = source
            self.destination = destination

        def __eq__(self, other):
            return self.source == other.source and self.destination == other.destination

        def __repr__(self):
            return f"Source: {self.source} Destination: {self.destination}"

        __str__ = __repr__

    class Path:
        """
        Class representing a Path through the Graph
        """
        __slots__ = ['vertices']

        def __init__(self, vertices=[]):
            """
            DO NOT EDIT THIS METHOD!
            Class representing a path in a graph
            :param vertices: Ordered list of vertices that compose the path
            """
            self.vertices = vertices

        def __eq__(self, other):
            return self.vertices == other.vertices

        def __repr__(self):
            return f"Path: {' -> '.join([str(v) for v in self.vertices])}\n"

        __str__ = __repr__

        def add_vertex(self, vertex):
            """
            adds a vertex id to the path
            :param vertex: vertex id
            :return: None
            """

            self.vertices.append(vertex)

        def remove_vertex(self):
            """
            removes the last vertex added to the path
            :return: None
            """
            if not self.is_empty():
                self.vertices.pop()

        def last_vertex(self):
            """
            fetches the most recent vertex
            :return: A vertex id
            """
            if self.is_empty():
                return None
            return self.vertices[-1]

        def is_empty(self):
            """
            checks to see if the path is empty
            :return: True if empty, else False
            """
            if len(self.vertices) == 0:
                return True
            return False

    class Vertex:
        """
        Class representing a Vertex in the Graph
        """
        __slots__ = ['ID', 'edges', 'visited', 'fake']

        def __init__(self, ID):
            """
            Class representing a vertex in the graph
            :param ID : Unique ID of this vertex
            """
            self.edges = []
            self.ID = ID
            self.visited = False
            self.fake = False

        def __repr__(self):
            return f"Vertex: {self.ID}"

        __str__ = __repr__

        def __eq__(self, other):
            """
            DO NOT EDIT THIS METHOD
            :param other: Vertex to compare
            :return: Bool, True if same, otherwise False
            """
            if self.ID == other.ID and self.visited == other.visited:
                if self.fake == other.fake and len(self.edges) == len(other.edges):
                    edges = set((edge.source.ID, edge.destination) for edge in self.edges)
                    difference = [e for e in other.edges if (e.source.ID, e.destination) not in edges]
                    if len(difference) > 0:
                        return False
                    return True

        def add_edge(self, destination):
            """
            adds an edge to the path
            :param destination: the destination vertex ID
            :return: None
            """
            new_edge = Graph.Edge(self, destination)
            if new_edge in self.edges:
                return None
            self.edges.append(new_edge)

        def degree(self):
            """
            checks the number of edges in the vertex
            :return: the number of edges
            """

            return len(self.edges)

        def get_edge(self, destination):
            """
            checks to see if the edge is in the vertex
            :param destination: the vertex ID to check for
            :return: the edge if found, else None
            """

            for e in self.edges:
                if e.destination == destination:
                    return e
            return None

        def get_edges(self):
            """
            :return: a list of all of the edges
            """

            return self.edges

        def set_fake(self):
            """
            sets the status of the vertex to fake
            :return: None
            """

            self.fake = True

        def visit(self):
            """
            sets the visited status to true
            :return: None
            """

            self.visited = True

        def remove_edge(self,target):
            """
            removes the edge with the target ID
            :param target: the target ID
            :return: None
            """
            for edge in self.edges:
                if edge.destination == target:
                    self.edges.remove(edge)

    def __init__(self, size=0, connectedness=1, filename=None):
        """
        DO NOT EDIT THIS METHOD
        Construct a random DAG
        :param size: Number of vertices
        :param connectedness: Value from 0 - 1 with 1 being a fully connected graph
        :param: filename: The name of a file to use to construct the graph.
        """
        assert connectedness <= 1
        self.adj_list = {}
        self.size = size
        self.connectedness = connectedness
        self.filename = filename
        self.construct_graph()

    def __eq__(self, other):
        """
        DO NOT EDIT THIS METHOD
        Determines if 2 graphs are IDentical
        :param other: Graph Object
        :return: Bool, True if Graph objects are equal
        """
        if len(self.adj_list) == len(other.adj_list):
            for key, value in self.adj_list.items():
                if key in other.adj_list:
                    if not self.adj_list[key] == other.adj_list[key]:
                        return False
                else:
                    return False
            return True
        return False

    def generate_edges(self):
        """
        DO NOT EDIT THIS METHOD
        Generates directed edges between vertices to form a DAG
        :return: A generator object that returns a tuple of the form (source ID, destination ID)
        used to construct an edge
        """
        random.seed(10)
        for i in range(self.size):
            for j in range(i + 1, self.size):
                if random.randrange(0, 100) <= self.connectedness * 100:
                    yield [i, j]

    def get_vertex(self, ID):
        """
        finds the vertex in the graph
        :param ID: the ID of the vertex
        :return: the vertex object
        """
        return self.adj_list.get(ID)

    def construct_graph(self):
        """
        takes in either a file to create a graph or creates its own graph
        :return: None
        """
        if self.filename is None:
            if self.size > 0 and (0 < self.connectedness <= 1):
                edges = self.generate_edges()
                for pair in edges:
                    if (pair[0] in self.adj_list) and (pair[1] in self.adj_list):
                        self.adj_list[pair[0]].add_edge(pair[1])
                    if (not pair[0] in self.adj_list) and (not pair[1] in self.adj_list):
                        if pair[0] == pair[1]:
                            v1 = Graph.Vertex(pair[0])
                            v1.add_edge(pair[1])
                            self.adj_list[pair[0]] = v1
                        else:
                            v1 = Graph.Vertex(pair[0])
                            v1.add_edge(pair[1])
                            self.adj_list[pair[0]] = v1
                            v2 = Graph.Vertex(pair[1])
                            self.adj_list[pair[1]] = v2
                    if (pair[0] in self.adj_list) and (not pair[1] in self.adj_list):
                        v2 = Graph.Vertex(pair[1])
                        self.adj_list[pair[0]].add_edge(pair[1])
                        self.adj_list[pair[1]] = v2
                    if (not pair[0] in self.adj_list) and (pair[1] in self.adj_list):
                        v1 = Graph.Vertex(pair[0])
                        v1.add_edge(pair[1])
                        self.adj_list[pair[0]] = v1
            else:
                raise GraphError()
            return
        try:
            file = open(self.filename, "r", encoding="utf-8")
            for line in file:
                pair = [int(num) for num in line.split() if line]
                if (pair[0] in self.adj_list) and (pair[1] in self.adj_list):
                    self.adj_list[pair[0]].add_edge(pair[1])
                if (not pair[0] in self.adj_list) and (not pair[1] in self.adj_list):
                    if pair[0] == pair[1]:
                        v1 = Graph.Vertex(pair[0])
                        v1.add_edge(pair[1])
                        self.adj_list[pair[0]] = v1
                    else:
                        v1 = Graph.Vertex(pair[0])
                        v1.add_edge(pair[1])
                        self.adj_list[pair[0]] = v1
                        v2 = Graph.Vertex(pair[1])
                        self.adj_list[pair[1]] = v2
                if (pair[0] in self.adj_list) and (not pair[1] in self.adj_list):
                    v2 = Graph.Vertex(pair[1])
                    self.adj_list[pair[0]].add_edge(pair[1])
                    self.adj_list[pair[1]] = v2
                if (not pair[0] in self.adj_list) and (pair[1] in self.adj_list):
                    v1 = Graph.Vertex(pair[0])
                    v1.add_edge(pair[1])
                    self.adj_list[pair[0]] = v1

        except FileNotFoundError:
            raise GraphError()

        self.size = len(self.adj_list)

    def BFS(self, start, target):
        """
        uses breadth first search iteratively to find a path from start to target
        :param start: the start vertex
        :param target: the target vertex
        :return: A path object with the path from start to target
        """
        if (start not in self.adj_list) or (target not in self.adj_list):
            return Graph.Path([])

        start_p = Graph.Path([])
        start_p.add_vertex(start)
        queue = [start_p]

        while queue:
            p = queue.pop()
            vertex = p.last_vertex()
            if vertex == target:
                return p
            elif not self.adj_list[vertex].visited:
                for e in self.adj_list[vertex].edges:
                    v = list(p.vertices)
                    new_path = self.Path(v)
                    new_path.add_vertex(e.destination)
                    queue.append(new_path)
                self.adj_list[vertex].visit()
        return Graph.Path([])

    def DFS(self, start, target, path=Path()):
        """
        Uses depth first search recursively to find a path from one vertex to another
        :param start: the start vertex
        :param target: the end vertex
        :param path: A Path object that represents the path from vertex start to target
        :return: the Path object
        """
        if (start not in self.adj_list) or (target not in self.adj_list):
            return path
        path.add_vertex(start)
        self.adj_list[start].visit()
        for e in self.adj_list[start].edges:
            while not self.adj_list[e.destination].visited:
                path = self.DFS(e.destination, target, path)
                if path.last_vertex() != target:
                    path.remove_vertex()

        return path


def fake_emails(graph, mark_fake=False):
    """
    finds all verticies with no outgoing edges and sets adds them to a list.
    :param graph: the graph with vertices
    :param mark_fake: if True, marks all fake vertices fake attribute to True
    :return:
    """
    fake_lst = []
    for vert in graph.adj_list.values():
        if vert.degree() == 0:
            fake_lst.append(vert.ID)
            if mark_fake:
                vert.set_fake()

    def check_fake_emails(start, emails=list()):
        """
        from a start vertex, remove all fake vertices that it can reach
        :param start: start vertex
        :param emails: the the fake vertex list
        :return: the new edge list
        """
        vertex = graph.get_vertex(start)
        vertex.visit()
        for edge in vertex.edges[:]:
            if edge.destination in emails:
                vertex.remove_edge(edge.destination)
        return vertex.edges

    for key in graph.adj_list.keys():
        graph.adj_list[key].edges = check_fake_emails(key,fake_lst)

    return fake_lst
