import tkinter

g = []


def dfs(v):
    global g, parent
    for i in range(len(g[v])):
        to = g[v][i]
        if to != parent[v]:
            parent[to] = v
            dfs(to)


def prufer_code():
    global parent, g, degree
    result = []
    parent[n - 1] = -1
    dfs(n - 1)
    ptr = -1
    for i in range(n):
        degree[i] = len(g[i])
        if degree[i] == 1 and ptr == -1:
            ptr = i
    leaf = ptr
    for it in range(n - 2):
        next = parent[leaf]
        result.append(next)
        degree[next] = degree[next] - 1
        if degree[next] == 1 and next < ptr:
            leaf = next
        else:
            ptr += 1
            while ptr < n and degree[ptr] != 1:
                ptr += 1
            leaf = ptr
    return result


def prufer_decode(code, m):
    vertices = m
    out = []
    vertex_set = [0 for i in range(vertices)]

    for i in range(vertices - 2):
        vertex_set[code[i] - 1] += 1

    for i in range(vertices - 2):
        for j in range(vertices):
            if vertex_set[j] == 0:
                vertex_set[j] = -1
                out.append([(j+1), code[i]])
                vertex_set[code[i] - 1] -= 1
                break

    add, j = [], 0
    for i in range(vertices):
        if vertex_set[i] == 0 and j == 0:
            add.append(i+1)
            j += 1
        elif vertex_set[i] == 0 and j == 1:
            add.append(i+1)
    out.append(add)
    return out


# 1 4, 5 7, 2 5, 6 8, 6 9, 2 6, 1 2, 3 1, 3 10
g = [[3, 1, 2], [0, 4, 5], [0, 9], [0], [1, 6], [1, 7, 8], [4], [5], [5], [2]]

parent = [-1 for i in range(len(g))]
degree = [-1 for i in range(len(g))]
n = len(g)

a = prufer_code()
a = [a[i] + 1 for i in range(len(a))]
b = prufer_decode(a, n)
print("Код Прюффера: ", *a)
print("Ребра дерева: ", *b)
