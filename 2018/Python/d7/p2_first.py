class Node:
    def __init__(self):
        self._in = {}
        self.out = {}

def complete_job(v, ans, graph):

    ans.append(v)

    rem_in    = []
    rem_graph = []

    # remove its connections
    for dest in graph[v].out:
        del graph[dest]._in[v]
        rem_in.append( (dest, v) )

    # del graph[v]
    rem_graph.append(v)

    while len(rem_in) != 0:
        dest, v = rem_in.pop()
        del graph[dest]._in[v]

    while len(rem_graph) != 0:
        del graph[rem_graph.pop()]

def dec_worker(workers, value):
    for i in range(len(workers)):
        workers[i] -= value

def min_worker(workers):

    best, index = float("inf"), 0
    for i, w in enumerate(workers):

        if w < best:
            best = w
            index = i

    return index, best

def free_worker(workers):

    for i, w in enumerate(workers):
        if w == 0: return i

    return 10

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
    workers = [0 for x in range(5)]
    project = ["" for x in range(5)]
    progress = {}
    total_time = 0
    assignment = True
    while len(graph) != 0:

        w = free_worker(workers)
        if w == 10 or (assignment == False):
            i, time = min_worker(workers)
            dec_worker(workers, time)
            total_time += time
            w = i
            complete_job(project[w], ans, graph) # worker_id, job, ans_key

        assignment = False
        for v in sorted(graph.keys()): # alph
            if len(graph[v]._in) == 0:

                if v in progress: continue

                # schedule the job
                workers[w] = 60 + (ord(v) - ord("A")) + 1
                project[w] = v
                progress[v] = True
                assignment = True
                break

    # 17
    # 348
    # 519
    # 423
    return total_time + max(workers)

# main
ans = sol()
print(ans)
