'''import matplotlib.pyplot as plt
import json
Node = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    # annotate是关于一个数据点的文本
    # nodeTxt为要显示的文本，centerPt为文本的中心点，箭头所在的点，parentPt为指向文本的点
    createPlot.ax1.annotate(nodeTxt, xy=parentPt,  xycoords='axes fraction',
             xytext=centerPt, textcoords='axes fraction',
             va="center", ha="center", bbox=nodeType, arrowprops=arrow_args )

def createPlot():
    a = (1,1)
    b = (a[0]+0.2,a[1]+0.4)
    c = (a[0]+0.2*2,a[1]+0.4*2)
    head = (10,10)
    l = ['1','0','0','1','1','0']
    fig = plt.figure(1,figsize=(5,5),facecolor='white') # 定义一个画布，背景为白色
    fig.clf() # 把画布清空
    # createPlot.ax1为全局变量，绘制图像的句柄，subplot为定义了一个绘图，
    #111表示figure中的图有1行1列，即1个，最后的1代表第一个图
    # frameon表示是否绘制坐标轴矩形

    createPlot.ax1 = plt.subplot(555,frameon=True)
    for i in range(1,len(l)):
        if(l[i] == '0'):
            if(l[i-1] == '0'):
                plotNode('testl',(3.5,2),(5,5),Node)
                     else:
                plotNode('testl',(head[0] + 0.1 * i, head[1] - 0.2 * i),(head[0] - 0.1 * (i - 1), head[1] - 0.2 * (i - 1)), Node)
        else:
            if (l[i - 1] == '0'):
                plotNode('testr', (head[0] - 0.1 * i, head[1] - 0.2 * i),(head[0] - 0.1 * (i - 1), head[1] - 0.2 * (i - 1)), Node)
            else:
                plotNode('testr', (head[0] + 0.1 * i, head[1] - 0.2 * i),(head[0] - 0.1 * (i - 1), head[1] - 0.2 * (i - 1)), Node)
    #plotNode('a decision node',a,b,Node)
    #plotNode('test',b,c,Node)
    #plotNode('a leaf node',(0.8,0.1),(0.3,0.8),leafNode)
    plt.show()
createPlot()
f = open('hfmTree.json')
g = json.loads(f.read())
#print(type(g['W']))
#print(type(g))
#def draw(key,value):

#for key in g.keys:'''
import matplotlib.pyplot as plt

plt.figure(1, figsize=(3, 3))
ax = plt.subplot(111,frameon=False)


'''arrowprops = {
    arrowstyle 箭头类型
    connectionstyle：xy与xytext连接之间类型
}'''


l = ['1','1','1','0','1']
head = (0,40)
for i in range(len(l)-1):
    if(l[i] == '1'):
        ax.annotate("node",
                    xy=(head[0]+10*(i+1), head[1]-20*(i+1)), xycoords='data',
                    xytext=(head[0]+10*i, head[1]-20*i), textcoords='data',
                    arrowprops=dict(arrowstyle="->",
                                    connectionstyle="arc3"),
                    )
ax.set_xlim(-40, 40)
ax.set_ylim(-100, 40)
plt.show()