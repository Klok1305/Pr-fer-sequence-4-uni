def dfs(v):
    global g, parent
    for i in range(len(g[v])):
        to = g[v][i]
        if to != parent[v]:
            parent[to] = v
            dfs(to)


def prufer_code(g):  # Асимптотика O(n)
    global parent, connections, n
    result = []
    parent[n - 1] = -1  # parent[номер родителя] = ребенок
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


def prufer_decode(code, m):
    vertices = m
    out = []
    node_in_code = [0 for i in range(vertices)]

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

#  Примеры данных
# 2 3 5 ; 1 ; 1 ; 5 ; 1 4 <=> 1 1 5
# 4 2 3 ; 1 5 6; 1 10 ; 1 ; 2 7 ; 2 8 9 ; 5 ; 6 ; 6 ; 3 <=> 1 5 2 6 6 2 1 3
#g = [[1, 2, 4], [0], [0], [4], [0, 3]]
# g = [[3, 1, 2], [0, 4, 5], [0, 9], [0], [1, 6], [1, 7, 8], [4], [5], [5], [2]]
g = []

while True:
    print('Введите 1 для кодировки дерева, 0 для декодировки, -1 для выхода')
    _ = int(input())
    if _ < 0:
        break
    elif _ == 1:
        print("Введите кол-во вершин: ")
        n = int(input())
        for i in range(n):
            print(f'Введите связи {i + 1}-oй вершины через пробел')
            g.append([int(el) - 1 for el in input().split()])
        parent = [-1 for i in range(len(g))]
        connections = [-1 for i in range(len(g))]
        a = prufer_code(g)
        a = [a[i] + 1 for i in range(len(a))]
        print("Код Прюфера: ", *a)
    elif _ == 0:
        print("Введите код Прфера через пробел")
        __ = input().split()
        code1 = [int(el) for el in __]
        b = prufer_decode(code1, len(code1) + 2)
        print("Ребра дерева: ", *b)


'''parent = [-1 for i in range(len(g))]
n = len(g)
connections = [-1 for i in range(len(g))]
a = prufer_code(g)
a = [a[i] + 1 for i in range(len(a))]
print("Код Прюфера: ", *a)'''