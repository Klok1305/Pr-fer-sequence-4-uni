import wx
import wx.xrc

Graph1 = []
Code1 = -1


class MApp(wx.App):
    def OnInit(self):
        self.frame = Frame1(None)
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True


class Frame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Кодирование и декодирование Прюфера",
                          size=wx.Size(800, 500))
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))
        myGridSizer = wx.GridSizer(0, 2, 0, 0)

        self.CodeLabel = wx.StaticText(self, wx.ID_ANY, u"Код Прюфера", size=(300, -1))
        self.CodeLabel.Wrap(-1)
        myGridSizer.Add(self.CodeLabel, 0, wx.ALL, 5)

        self.CodeText = wx.TextCtrl(self, wx.ID_ANY, "", size=(300, -1))
        myGridSizer.Add(self.CodeText, 0, wx.ALL, 5)

        self.GraphLabel = wx.StaticText(self, wx.ID_ANY, u"Граф", wx.DefaultPosition, wx.DefaultSize, 0)
        self.GraphLabel.Wrap(-1)
        myGridSizer.Add(self.GraphLabel, 0, wx.ALL, 5)

        self.GraphText = wx.TextCtrl(self, wx.ID_ANY, "", size=(300, -1))
        myGridSizer.Add(self.GraphText, 0, wx.ALL, 5)

        self.GetBtn = wx.Button(self, wx.ID_ANY, u"Закондировать дерево", wx.Point(-1, -1), wx.DefaultSize, 0)
        myGridSizer.Add(self.GetBtn, 0, wx.ALL, 5)

        self.SetBtn = wx.Button(self, wx.ID_ANY, u"Раскодировать дерево", wx.Point(-1, -1), wx.DefaultSize, 0)
        myGridSizer.Add(self.SetBtn, 0, wx.ALL, 5)

        self.SetSizer(myGridSizer)
        self.Layout()
        self.Centre(wx.BOTH)

        # Ввод

        self.GetBtn.Bind(wx.EVT_BUTTON, self.CodeTree)
        self.SetBtn.Bind(wx.EVT_BUTTON, self.DecodeTree)

    def CodeTree(self, event):
        Graph1 = self.GraphText.Value
        g = Graph1.split()
        for i in range(len(g)):
            g[i] = g[i].split(",")
            for j in range(len(g[i])):
                g[i][j] = int(g[i][j])
        print(g)
        a = prufer_code(g)
        a = [a[i] + 1 for i in range(len(a))]
        a = str(a)
        self.CodeText.Value = a

    def DecodeTree(self, event):
        code = self.CodeText.Value
        code, n = code.split(";")[0], int(code.split(";")[1])
        a_c = [int(el) for el in code.split()]
        k = str(prufer_decode(a_c, n))
        self.GraphText.Value = k


def dfs(v):
    global g, parent
    for i in range(len(g[v])):
        to = g[v][i]
        if to != parent[v]:
            parent[to] = v
            dfs(to)


def prufer_code(g):
    global parent, degree
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
                out.append([(j + 1), code[i]])
                vertex_set[code[i] - 1] -= 1
                break

    add, j = [], 0
    for i in range(vertices):
        if vertex_set[i] == 0 and j == 0:
            add.append(i + 1)
            j += 1
        elif vertex_set[i] == 0 and j == 1:
            add.append(i + 1)
    out.append(add)
    return out

    # 1 4, 5 7, 2 5, 6 8, 6 9, 2 6, 1 2, 3 1, 3 10

# 3,1,2 0,4,5 0,9 0 1,6 1,7,8 4 5 5 2 ========== Дерево
# 1 5 2 6 6 2 1 3;10 ======== Код
# g = [[1, 2, 4], [0], [0], [4], [0, 3]]
g = [[3, 1, 2], [0, 4, 5], [0, 9], [0], [1, 6], [1, 7, 8], [4], [5], [5], [2]]



parent = [-1 for i in range(len(g))]
degree = [-1 for i in range(len(g))]
n = len(g)

a = prufer_code(g)
a = [a[i] + 1 for i in range(len(a))]
b = prufer_decode(a, n)
print("Код Прюфера: ", *a)
print("Ребра дерева: ", *b)

app = MApp(False)
app.MainLoop()
