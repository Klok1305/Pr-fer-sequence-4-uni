def dfs(v):
    global g, parent
    for i in range(len(g[v])):
        to = g[v][i]
        if to != parent[v]:
            parent[to] = v
            dfs(to)


parent, connections, n = [], [], 0


def prufer_code(g):
    result = []
    parent[n - 1] = -1
    dfs(n - 1)
    node = -1
    for i in range(n):
        connections[i] = len(g[i])
        if connections[i] == 1 and node == -1:
            node = i

    leaf = node
    for it in range(n - 2):
        current_parent = parent[leaf]
        result.append(current_parent)
        connections[current_parent] = connections[current_parent] - 1
        if connections[current_parent] == 1 and current_parent < node:
            leaf = current_parent
        else:
            node += 1
            while node < n and connections[node] != 1:
                node += 1
            leaf = node
    return result


vertices = 2
out = []
node_in_code = [0 for i in range(vertices)]


def prufer_decode(code, m):
    for i in range(vertices - 2):
        node_in_code[code[i] - 1] += 1
    for i in range(vertices - 2):
        for j in range(vertices):
            if node_in_code[j] == 0:
                node_in_code[j] = -1
                out.append([(j + 1), code[i]])
                node_in_code[code[i] - 1] -= 1
                break
    add, j = [], 0
    for i in range(vertices):
        if node_in_code[i] == 0 and j == 0:
            add.append(i + 1)
            j += 1
        elif node_in_code[i] == 0 and j == 1:
            add.append(i + 1)
    out.append(add)
    return out
