'''import queue


def bfs(adj, start):
    visited = set()
    q = queue.Queue()
    q.put(start)
    while not q.empty():
        u = q.get()
        print(u)
        for v in adj.get(u, []):
            if v not in visited:
                visited.add(v)
                q.put(v)


graph = {1: [4, 2], 2: [3, 4], 3: [4], 4: [5]}
bfs(graph, 1)'''
import pygraphviz as pgv
A=pgv.AGraph(directed=True,strict=True)
A.add_edge(1,2)
A.add_edge(1,3)
A.add_edge(2,4)
A.add_edge(2,5)
A.add_edge(5,6)
A.add_edge(5,7)
A.add_edge(3,8)
A.add_edge(3,9)
A.add_edge(76,'c')
A.add_edge(8,11)
A.graph_attr['epsilon']='0.01'
#print A.string() # print dot file to standard output
A.write('fooOld.dot')
A.layout('dot') # layout with dot
A.draw('a.png') # write to file
