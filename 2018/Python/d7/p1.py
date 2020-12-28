class Node:
    def __init__(self):
        self._in = {}
        self.out = {}

def sol():
    data = [x.strip() for x in open("d7.txt").readlines()]

    graph = {}

    for row in data:

        # Step W must be finished before step B can begin
        row  = row.split(" ")
        a, b = row[1], row[7]

        if not a in graph: graph[a] = Node()
        if not b in graph: graph[b] = Node()

        graph[b]._in[a] = True
        graph[a].out[b] = True

    ans = []
    while len(graph) != 0:

        rem_in    = []
        rem_graph = []

        #print(list(sorted(graph.keys())))
        print(list(filter(lambda x: len(graph[x]._in) == 0, sorted(graph.keys()))))
        for v in sorted(graph.keys()): # alph hopefully
            if len(graph[v]._in) == 0:

                # remove its connections
                for dest in graph[v].out:
                    # del graph[dest]._in[v]
                    rem_in.append( (dest, v) )

                # remove the node with no in degree
                ans.append(v)
                # del graph[v]
                rem_graph.append(v)
                break

        while len(rem_in) != 0:
            dest, v = rem_in.pop()
            del graph[dest]._in[v]

        while len(rem_graph) != 0:
            del graph[rem_graph.pop()]

    # WGRBKZVESDYPMATUXCFIQJLHNO
    # GRWBEKVZDSYAMPTUCFIXQJLHNO
    return "".join(ans)

# main
ans = sol()
print(ans)
