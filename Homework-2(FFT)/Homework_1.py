def check_bipartite(adj):
    n = len(adj)
    color = [-1] * n

    for start in range(n):
        if color[start] != -1:
            continue
        color[start] = 0
        queue = [start]
        while queue:
            current = queue.pop(0)
            for neighbor in adj[current]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[current]
                    queue.append(neighbor)
                elif color[neighbor] == color[current]:
                    return None

    left  = [i for i, c in enumerate(color) if c == 0]
    right = [i for i, c in enumerate(color) if c == 1]
    return left, right

def kuhn_match(adj, left):
    n = len(adj)
    match_u = [-1] * n
    used = [False] * n

    def dfs(u):
        for v in adj[u]:
            if not used[v]:
                used[v] = True
                if match_u[v] == -1 or dfs(match_u[v]):
                    match_u[v] = u
                    return True
        return False

    for u in left:
        used[:] = [False] * n
        dfs(u)
    return match_u

def orient_edges(adj, left, match_u):
    n = len(adj)
    directed = [[] for _ in range(n)]
    for u in left:
        for v in adj[u]:
            if match_u[v] == u:
                directed[v].append(u)
            else:
                directed[u].append(v)
    return directed

def min_vertex_cover(adj):
    parts = check_bipartite(adj)
    if parts is None:
        return "Граф не является двудольным"

    left, right = parts

    match_u = kuhn_match(adj, left)

    directed = orient_edges(adj, left, match_u)

    n = len(adj)
    visited = [False] * n
    stack = [u for u in left if all(match_u[v] != u for v in adj[u])]
    for u in stack:
        visited[u] = True

    while stack:
        u = stack.pop()
        for v in directed[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)

    L_minus = [u for u in left  if not visited[u]]
    R_plus  = [v for v in right if visited[v]]
    return L_minus + R_plus


graph = {
    0: [1, 3, 5],
    1: [0, 2, 6],
    2: [1],
    3: [0, 4],
    4: [3, 5, 7],
    5: [0, 4],
    6: [1],
    7: [4]
}

print(min_vertex_cover(graph))
