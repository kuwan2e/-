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
class imageNode(object):
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
        self.marked = 0


    def allmarked(self):
        temp = self
        while (temp != None):
            if (temp.marked == 1):
                temp = temp.next
            else:
                return 0
        return 1

def dfs(image, i, j):
    m = Stack()
    m.push(image[i])
    temp = image[i].next
    #print("(", m.peek().data, end=",")
    while (m.is_empty() != True):
        #print(m.peek().data)
        m.peek().marked = 1
        if (temp != None):
            print("(", m.peek().data, end=",")
            if(temp.marked == 0):
                m.push(image[temp.data])
                m.peek().marked = 1
                if (m.peek().data == j):
                    print(j,")")
                    return 1
                else:
                    if (m.peek().next == None):
                        print(m.peek().data, ")", end=" -> ")
                        m.pop()
                    else:
                        print(m.peek().data,")",end=" -> ")
                        #return dfs(image, m.peek().data, j)
                        m.push(image[m.peek().data])
                        temp = image[m.peek().data]
            temp = temp.next
        else: m.pop()
    #print("(",m.peek().data,end=",")
    return 0
def bfs(image,i,j):
    m = Queue()
    m.add(image[i])
    m.peek().marked = 1
    temp = image[i].next
    while (temp != None):
        print(m.peek().data)
        if (temp.marked == 0):
            m.add(image[temp.data])
            m.peek().marked = 1
            if (temp.data == j): return 1
            temp = temp.next
        else:
            temp = temp.next
    m.pop()
    while(m.is_empty() != True):
        if (m.peek().next == None):
            m.pop()
        else:
            return bfs(image, m.peek().data, j)
    return 0
def dfsimg(V, i):
    m = Stack()
    temp = V[i]
    temp.marked = 1
    m.push(temp)
    while(m.is_empty() != True):
        #print(m.peek().data)
        temp = V[temp.data]
        temp = temp.next
        if(temp != None):
            if (V[temp.data].marked == 0):
                temp.marked = 1
                V[temp.data].marked = 1
                print("(",m.peek().data,end=",")
                m.push(V[temp.data])
                print(m.peek().data,")")
            else:
                temp = temp.next
                temp.marked = 1
        if(m.peek().allmarked() == 1): m.pop()
    #print("(",m.peek().data,end=",")
    return 0


