import pygraphviz as pgv
A=pgv.AGraph(directed=True,strict=True)
s = "101010"
c = "101011"
lt = list(s)
print(lt)
a = ["node"]
for ls in lt:
    str1 = "".join(a)
    a.append(ls)
    str2 = "".join(a)
    A.add_edge(str1,str2)
lt = list(c)
print(lt)
a = ["node"]
for ls in lt:
    str1 = "".join(a)
    a.append(ls)
    str2 = "".join(a)
    A.add_edge(str1,str2)
A.graph_attr['epsilon']='0.01'
#print A.string() # print dot file to standard output
A.write('fooOld.dot')
A.layout('dot') # layout with dot
A.draw('a.png') # write to file
