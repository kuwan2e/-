import numpy as np
from operator import itemgetter
class sparse_matrix(object):
    def __init__(self):
        self.data = []
        self.rpos = []
        self.mu = 0
        self.nu = 0
        self.tu = 0
        self.juzhen = [[]]
    def RLSM(self,s):
        data1 = []
        for m in s:
            data1.append(m)
        data = sorted(data1,key=itemgetter(0,1),reverse=False)
        #print(data)
        self.data = data
        n = 0
        mu = 1
        nu = 1
        for i in range(0,len(data)):
            if (data[i][0] > mu):
                mu = data[i][0]
            if (data[i][1] > nu): nu = data[i][1]
            n += 1
        self.mu = mu
        self.nu = nu
        self.tu = n
        rpos = np.zeros(mu+1,dtype=int)
        juzhen = np.zeros((mu+1,nu+1))
        k = 0
        for d in data:
            # print(d)
            t = d[0]
            k += 1
            if (rpos[t] == 0):
                rpos[t] = k
            juzhen[d[0]][d[1]] = d[2]
        self.rpos = rpos

        self.juzhen = juzhen
    def sortdata(self):
        self.data = sorted(self.data, key=itemgetter(0, 1), reverse=False)
    def RLSMself(self):
        if(self.data != []):
            data = self.data
            n = 0
            mu = 1
            nu = 1
            for i in range(0, len(data)):
                if (data[i][0] > mu):
                    mu = data[i][0]
                if (data[i][1] > nu): nu = data[i][1]
                n += 1
            self.mu = mu
            self.nu = nu
            self.tu = n
            rpos = np.zeros(mu + 1,dtype=int)
            juzhen = np.zeros((mu + 1, nu + 1))
            k = 0
            for d in data:
                # print(d)
                t = d[0]
                k += 1
                if (rpos[t] == 0):
                    rpos[t] = k
                juzhen[d[0]][d[1]] = d[2]
            self.rpos = rpos
            self.juzhen = juzhen
        elif(self.juzhen != [[]]):
            self.mu = self.juzhen.shape[0] - 1
            self.nu = self.juzhen.shape[1] - 1
            for i in range(self.mu):
                for j in range(self.nu):
                    if(self.juzhen[i][j] != 0):
                        self.data.append((i,j,self.juzhen[i][j]))
def addSMatrix(M,N):
    Q = sparse_matrix()
    if(M.mu != N.mu or M.nu != N.nu): return "Error"
    else:
        for i in range (len(M.data)-1):
            for mdata in M.data:
                for ndata in N.data:
                    if (mdata[0] == ndata[0] and mdata[1] == ndata[1]):
                        Q.data.append((mdata[0], mdata[1], mdata[2] + ndata[2]))
                        M.data.remove(mdata)
                        N.data.remove(ndata)
                        break
        for mdata in M.data:
            Q.data.append(mdata)
        for ndata in N.data:
            Q.data.append(ndata)
    Q.RLSMself()
    return Q
def subtMatrix(M,N):
    Q = sparse_matrix()
    if (M.mu != N.mu or M.nu != N.nu):
        return "Error"
    else:
        for i in range (len(M.data)-1):
            for mdata in M.data:
                for ndata in N.data:
                    if (mdata[0] == ndata[0] and mdata[1] == ndata[1]):
                        Q.data.append((mdata[0], mdata[1], mdata[2] - ndata[2]))
                        M.data.remove(mdata)
                        N.data.remove(ndata)
                        break
        for mdata in M.data:
            Q.data.append(mdata)
        for ndata in N.data:
            Q.data.append((ndata[0],ndata[1],-ndata[2]))
    Q.RLSMself()
    return Q
def searchrpos(Q,i):
    if(i < Q.mu):
        if(Q.rpos[i+1] != 0):
            return Q.rpos[i+1] - Q.rpos[i]
        else:
            for j in range(i+1,Q.mu+1):
                if(Q.rpos[j] == 0):
                    continue
                else:
                    return Q.rpos[j] - Q.rpos[i]
    else:
        return Q.tu - Q.rpos[i] + 1
def multSMatrix(M,N):
    if(M.nu != N.mu): return "Error"
    else:
        Q = sparse_matrix()
        juzhen = np.zeros((M.mu+1,N.nu+1))
        for mdata in M.data:
            t = searchrpos(N,mdata[1])
            for i in range(N.rpos[mdata[1]],N.rpos[mdata[1]] + t):
                '''print(N.rpos[mdata[1]])
                print("t",t)
                print("mdata",mdata)'''
                juzhen[mdata[0]][N.data[i-1][1]] += N.data[i-1][2]*mdata[2]
        Q.juzhen = juzhen
        Q.RLSMself()
        return Q
def printMatrix(Q):
    for i in range(1,Q.mu+1):
        if(i == 1):print("「",end="")
        else: print("|",end="")
        for j in range(1,Q.nu+1):
            print(Q.juzhen[i][j],end=" ")
        if(i == Q.mu): print("」")
        else: print("|")
'''a = ((1,1,3),(1,2,3),(2,3,4),(3,2,4),(3,4,5),(4,6,6),(4,5,7))
b = ((1,6,4),(2,6,7),(4,2,2),(4,3,4),(4,6,5))
s = sparse_matrix()
s.RLSM(a)
A = sparse_matrix()
B = sparse_matrix()
A.RLSM(a)
print(A.juzhen)
B.RLSM(b)
Q = subtMatrix(A,B)
Q.RLSMself()
print(B.nu)
print(Q.juzhen)
printMatrix(Q)
print("Q.Mu",Q.mu)
print("tu" ,B.tu,B.rpos)
print(searchrpos(B,4))


T = sparse_matrix()
T.juzhen = np.zeros((3,4))
T.juzhen[1][3] = 4
T.RLSMself()
print(T.data)

print("————————————————————————————————————————")

c = ((1,1,5),(2,4,2))
d = ((1,2,4),(3,1,3),(4,3,2))
C = sparse_matrix()
D = sparse_matrix()
C.RLSM(c)
D.RLSM(d)
MM = multSMatrix(C,D)
print(MM.juzhen)
MM.RLSMself()
printMatrix(MM)'''
if __name__ == '__main__':
    a = ((1,1,4),(1,2,-3),(1,5,1),(2,4,8),(3,3,1),(4,5,70))
    b = ((1,1,3),(2,1,4),(2,2,2),(3,2,1),(4,1,1),(5,3,0))
    A = sparse_matrix()
    B = sparse_matrix()
    A.RLSM(a)
    B.RLSM(b)
    print(A.mu)
    print(B.mu)
    Q = multSMatrix(A,B)
    print(Q.juzhen)