from image import imageNode
import image
V = []
for i in range(4):
    a = imageNode(i + 1, None)
    V.append(a)

V.insert(0, imageNode(0, None))
temp2 = imageNode(3, None)
temp1 = imageNode(2, temp2)
V[1].next = temp1
temp1 = imageNode(4, None)
V[3].next = temp1
temp1 = imageNode(1, None)
V[4].next = temp1
for i in range(1,len(V)):
    j = i
    T = V[j]
    while(T.next!=None):
        print(T.data," -> ",end="")
        T=T.next
    print(T.data)
while(1):
    i = int(input("input i" + "\n"))
    j = int(input("input j" + "\n"))
    print("dfs结果为" + str(image.dfs(V, i, j)))
    i = int(input("input i" + "\n"))
    j = int(input("input j" + "\n"))
    print("bfs结果为" + str(image.bfs(V, i, j)))