import tu
import json

def outputVexSetNumToCities(vexset):
    To = []
    for vex in vexset:
        To.append(cities[str(vex)])
    print(To)
    return To
def outputArcSetNumToCities(arcset):
    To = []
    for arc in arcset:
        To.append((cities[str(arc[0])],cities[str(arc[1])]))
    print(To)
    return To
#print(dfsvexset,dfsarcset)
img = tu.initimg("image.json")
f = open("cities.json",encoding='UTF-8')
cities = json.load(f)
#print(cities)
dfsvexset,dfsarcset = tu.dfs(img)
bfsvexset,bfsarcset = tu.bfs(img)
print("深度优先遍历得到的vexset为",end="：")
outputVexSetNumToCities(dfsvexset)
print("深度优先遍历得到的arcset为",end="：")
outputArcSetNumToCities(dfsarcset)
print("广度优先遍历得到的vexset为",end="：")
outputVexSetNumToCities(bfsvexset)
print("广度优先遍历得到的arcset为",end="：")
outputArcSetNumToCities(bfsarcset)