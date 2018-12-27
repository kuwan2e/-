import numpy as np
class Image(object):
    def __init__(self,size):
        self.size = size
        self.juzhen = np.zeros((size,size),dtype=np.int)

def minitree(v):
    m = v.juzhen.max() + 1
    t = Image(v.size)
    for k in range(0,v.size):
        for n in range(0,v.size):
            if(v.juzhen[k][n] == 0): v.juzhen[k][n] = m
    c = 0
    while(c<v.size):
        for i in range(0, v.size):
            for j in range(i+1, v.size):
                if (v.juzhen[i][j] == v.juzhen.min() and v.juzhen.min() != v.juzhen.max()):
                    #print(v.juzhen.min())
                    # 遍历i
                    ti = []
                    tj = []
                    for ii in range(0, v.size):
                        if (t.juzhen[i][ii] != 0):
                            ti.append(ii)
                    # 遍历j
                    for jj in range(0, v.size):
                        if (t.juzhen[j][jj] != 0):
                            tj.append(jj)
                    #print(ti, tj)
                    # 遍历i,j查找是否存在两顶点在同一分量上
                    s = 0
                    for o in ti:
                        for p in tj:
                            if (t.juzhen[o][p] != 0 or o == p):
                                s = 1
                                break
                    if (s == 0):
                        t.juzhen[i][j] = t.juzhen[j][i] = v.juzhen[i][j]
                    v.juzhen[i][j] = v.juzhen[j][i] = m
        c += 1
    return t
a = Image(6)
test = [6,1,5,0,0,5,0,3,0,5,6,4,0,2,6]
n=0
for i in range(0,6):
    for j in range(i+1,6):
        a.juzhen[i][j] = a.juzhen[j][i] = test[n]
        n+=1

'''def all(v):
    a = np.zeros(v.size)
    for i in range(0,6):
        for j in range(i+1,6):
            if(v.juzhen[i][j] != 0):
                a[i] = 1
                a[j] = 1
    if(a.min() == 0): return 0
    else: return 1'''

if __name__ == "__main__":
    print(a.juzhen)
    t = minitree(a)
    print(t.juzhen)