import json
class Stack(object):
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
class Queue(object):
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)
    def add(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop(0)
class ArcNode(object):
    adjvex = 0
    next = None
    def __init__(self,adjvex = 0,next = None):
        self.adjvex = adjvex
        self.next = next
class VNode(object):
    data = 0
    firstarc = None
    def __init__(self,data = 0,firstarc = None):
        self.data = data
        self.firstarc = firstarc
class ALGraph(object):
    Adjlist = []
    vexnum = 0
    arcnum = 0
    def __init__(self,Adjlist = []):
        sum = 0
        self.Adjlist = Adjlist
        for v in Adjlist:
            t = v.firstarc
            while(t != None):
                sum += 1
                t = t.next
        self.vexnum = len(Adjlist) - 1
        self.arcnum = int(sum/2)
def outputAdjlist(l = ALGraph.Adjlist):
    for i in range(1,len(l)):
        print(l[i].data,end="-->")
        t = l[i].firstarc
        while(t != None):
            if(t.next != None): print(t.adjvex,end="->")
            else: print(t.adjvex)
            t = t.next

def dfs(ALGraph = ALGraph,data = 1):
    vStack = Stack()
    arcset = []
    vexset = []
    flag = [0 for _ in range(ALGraph.vexnum+1)]
    vStack.push(ALGraph.Adjlist[data])
    temp = ALGraph.Adjlist[data].firstarc
    while(True):
        if(temp != None):
            if(flag[temp.adjvex] == 0):
                #flag[temp.adjvex] = 1
                if(flag[vStack.peek().data] == 0):
                    flag[vStack.peek().data] = 1
                    #print(vStack.peek().data)
                    vexset.append(vStack.peek().data)
                vStack.push(ALGraph.Adjlist[temp.adjvex])
                temp = vStack.peek().firstarc
                P = vStack.pop()
                arcset.append((vStack.peek().data, P.data))
                vStack.push(P)
            else:
                if (flag[vStack.peek().data] == 0):
                    flag[vStack.peek().data] = 1
                    #print(vStack.peek().data)
                    vexset.append(vStack.peek().data)
                temp = temp.next
        else:
            vStack.pop()
            if(vStack.is_empty() == True): break
            temp = vStack.peek().firstarc.next
    return vexset,arcset
def initArc(str=str):
    l = str.split(",")
    h = ArcNode
    c = ArcNode
    h = c
    for i in range(len(l)):
        t = ArcNode(int(l[i]))
        c.next = t
        c = c.next
    return h.next
def initimg(imgfile):
    initjson = open(imgfile,encoding='UTF-8')
    init = json.load(initjson)
    imgV = [VNode for i in range(len(init) + 1)]
    for key in init.keys():
        #print(key)
        imgV[int(key)] = VNode(int(key))
        imgV[int(key)].firstarc = initArc(init[key])
    return ALGraph(imgV)
def bfs(ALGraph = ALGraph,data = 1):
    vQueue = Queue()
    arcset = []
    vexset = []
    flag = [0 for _ in range(ALGraph.vexnum + 1)]
    for i in range(data,len(ALGraph.Adjlist)):
        if(flag[ALGraph.Adjlist[i].data] == 0):
            flag[ALGraph.Adjlist[i].data] = 1
            #print("1,,",ALGraph.Adjlist[i].data)
            vexset.append(ALGraph.Adjlist[i].data)
            vQueue.add(ALGraph.Adjlist[i])
            while(vQueue.is_empty() != True):
                u = vQueue.pop()
                temp = u.firstarc
                while(temp != None):
                    if(flag[temp.adjvex] == 0):
                        flag[temp.adjvex] = 1
                        #print("2,,",temp.adjvex)
                        vexset.append(temp.adjvex)
                        arcset.append((u.data,temp.adjvex))
                        vQueue.add(ALGraph.Adjlist[temp.adjvex])
                    temp = temp.next
    return vexset,arcset
if __name__ == "__main__":
    V = []
    V.append(VNode)
    for i in range(1, 9):
        V.append(VNode(i))

    V[1].firstarc = ArcNode(2, ArcNode(3))
    V[2].firstarc = ArcNode(4, ArcNode(5, ArcNode(1)))
    V[3].firstarc = ArcNode(6, ArcNode(7, ArcNode(1)))
    V[4].firstarc = ArcNode(2, ArcNode(8))
    V[5].firstarc = ArcNode(8, ArcNode(2))
    V[6].firstarc = ArcNode(7, ArcNode(3))
    V[7].firstarc = ArcNode(6, ArcNode(3))
    V[8].firstarc = ArcNode(5, ArcNode(4))

    num = 0
    img = ALGraph(V)
    #bfs(img,4)
    c,d = bfs(img, 2)
    #outputAdjlist(V)
    print(c,d)
    test = initimg("image.json")
    vexset, arcset = bfs(test, 1)
    #bfs(test,1)
    print(vexset, arcset)