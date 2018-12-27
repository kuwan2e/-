import xishujuzhen as xsjz
from xishujuzhen import sparse_matrix as sm
def str_to_tuple(str):
    tupleresult=[]
    t = str.split('),(')
    for r in t:
        temp = r.replace('(', '').replace(')', '')
        a = tuple([int(i) for i in temp.split(',')])
        #print(a)
        tupleresult.append(a)
    return tuple(tupleresult)
o = '#'
while(o != 'e'):
    print("矩阵加法：1")
    print("矩阵减法：2")
    print("矩阵乘法：3")
    print("退出：e")
    o = input("请选择将要进行的矩阵运算")
    if (o == '1'):
        a = input("以三元组形式输入第一个矩阵，回车结束")
        b = input("以三元组形式输入第二个矩阵，回车结束")
        A = sm()
        B = sm()
        # print(str_to_tuple(a)))
        # print(str_to_tuple(b)))
        A.RLSM(str_to_tuple(a))
        B.RLSM(str_to_tuple(b))
        Q = xsjz.addSMatrix(A, B)
        print("运算结果为：————————————————————————————————————————————————————")
        xsjz.printMatrix(Q)
        print("——————————————————————————————————————————————————————————————")
    if (o == '2'):
        a = input("以三元组形式输入被减矩阵，回车结束")
        b = input("以三元组形式输入减矩阵，回车结束")
        A = sm()
        B = sm()
        A.RLSM(str_to_tuple(a))
        B.RLSM(str_to_tuple(b))
        Q = xsjz.subtMatrix(A, B)
        print("运算结果为：————————————————————————————————————————————————————")
        xsjz.printMatrix(Q)
        print("——————————————————————————————————————————————————————————————")
    if (o == '3'):
        a = input("以三元组形式输入第一个矩阵，回车结束")
        b = input("以三元组形式输入第二个矩阵，回车结束")
        A = sm()
        B = sm()
        A.RLSM(str_to_tuple(a))
        B.RLSM(str_to_tuple(b))
        Q = xsjz.multSMatrix(A, B)
        print("运算结果为：————————————————————————————————————————————————————")
        xsjz.printMatrix(Q)
        print("——————————————————————————————————————————————————————————————")
'''
(1,1,10),(2,3,9),(3,1,-1)
(2,3,-1),(3,1,1),(3,3,-3)
(1,1,10),(2,2,9),(3,1,-1)
(2,2,-1),(3,1,1),(3,2,-3)
(1,1,4),(1,2,-3),(1,5,1),(2,4,8),(3,3,1),(4,5,70)
(1,1,3),(2,1,4),(2,2,2),(3,2,1),(4,1,1),(5,3,0)
'''