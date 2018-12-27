'''dict1 = {
    'A' : 12,
    'B' : 15,
    ' ' : 111
}
d3 = {
    'D' : 44
}
d2 = dict1.copy()
print(list(d2.values()))
for key in d2.keys():
    d2[key] = str(d2[key]) + "1"
print(dict1)
print(d2.items())
d4 = {}
d4.update(d2)
d4.update(d3)
print(d4)'''
import json
'''hfmanTreeFile = "hfmTree.json"
initjson = open(hfmanTreeFile)
init = json.load(initjson)
print(init)
with open('tobe.txt') as f:
    strr = ""
    tobe = list(f.read())
    print(tobe)
    for t in tobe:
        if(t != '\n'):
            strr += init[t]
    print(strr)
    cf = open('CodeFile.txt','w')
    cf.write(strr)
    cf.close()
def decode(astr,hfmTreedict):
    for key in hfmTreedict.keys():
        if (astr == hfmTreedict[key]):
            return key
    return 0
with open('CodeFile.txt') as de:
    dec = list(de.read())
    decostr = ""
    decolist = []
    #print(dec)
    for e in dec:
        decostr += e
        if(decode(decostr,init) !=0):
            decolist.append(decode(decostr,init))
            decostr = ""
    print("".join(decolist))
'''
import tu

#print(type(init))

def initArc(str=str):
    l = str.split(",")
    h = tu.ArcNode
    c = tu.ArcNode
    h = c
    for i in range(len(l)):
        t = tu.ArcNode(int(l[i]))
        c.next = t
        c = c.next
    return h.next
def initimg(imgfile):
    initjson = open(imgfile)
    init = json.load(initjson)
    imgV = [tu.VNode for i in range(len(init) + 1)]
    for key in init.keys():
        #print(key)
        imgV[int(key)] = tu.VNode(int(key))
        imgV[int(key)].firstarc = initArc(init[key])
    return tu.ALGraph(imgV)
'''print(imgV[1].firstarc.next.next,end="\n\n\n")
tu.outputAdjlist(imgV)
test = tu.ALGraph(imgV)
print(test.vexnum)'''

test = initimg("image.json")
vexset,arcset = tu.dfs(test,1)
print(vexset,arcset)