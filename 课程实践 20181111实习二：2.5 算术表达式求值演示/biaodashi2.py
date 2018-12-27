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
    def delete(self):
        self.items = []
def operate(a,o,b):
    if(o == '*'): return a*b
    elif(o == '/'): return a/b
    elif(o == '+'): return a+b
    elif(o == '-'): return a-b
def precede(a,b):
    if(a != '#'):
        if(a == '+' or a == '-'):
            if(b == '+' or b == '-' or b == ')' or b == '#'):
                return '>'
            elif(b == '*' or b == '/' or b == '('):
                return '<'
        elif(a == '*' or a == '/'):
            if(b == '('):
                return '<'
            else: return '>'
        elif(a == '('):
            if(b == ')'):
                return '='
            else: return '<'
        elif(a == ')'):
            return '>'
    elif(a == '#'):
        if(b == '#'): return '='
        else:
            return '<'
intNumber = []
for n in range(10):
    intNumber.append(str(n))
def isInt(x):
    for n in intNumber:
        if(x == n): return 1
    return 0
def jisuan(s):
    #a = input("输入表达式:" + "\n")
    b = list(s)
    b.append('#')
    #print(b)
    OPTR = Stack()
    Number = Stack()
    operator = Stack()
    operator.push('#')
    i = 0
    NumberTemp = []
    while (True):
        print("本次输入为：", b[i],end='\t')
        print("运算符栈为：", operator.items, end='\t')
        if (b[i] == '*' or b[i] == '/' or b[i] == '+' or b[i] == '-' or b[i] == '(' or b[i] == ')' or b[i] == '#'):
            # print("nt",NumberTemp)
            if (NumberTemp != []):
                Nt = "".join(NumberTemp)
                Number.push(float(Nt))
                NumberTemp = []
            if (precede(operator.peek(), b[i]) == '<'):
                operator.push(b[i])
            elif (precede(operator.peek(), b[i]) == '='):
                x = operator.pop()
            elif (precede(operator.peek(), b[i]) == '>'):
                theta = operator.pop()
                x2 = Number.pop()
                x1 = Number.pop()
                print("运算", x1, theta, x2, end='\t')
                Number.push(operate(x1, theta, x2))
                i -= 1
        elif (isInt(b[i]) == 1 or b[i] == '.'):
            NumberTemp.append(b[i])
        elif(b[i] <= 'z' and b[i] >= 'A'):
            cTemp = b[i]
            b[i] = input("输入" + b[i] + "的值\n")
            for j in range(i,len(b)):
                if(b[j] == cTemp):
                    b[j] = b[i]
            NumberTemp.append(b[i])
        else:
            NumberTemp.append(b[i])
        # if (b[i] != '#'):
        print("运算数栈为：", Number.items, end='\n')

        i += 1
        # elif(b[i] == '#'):
        #
        if (operator.peek() == '#' and b[i] == '#'):
            print("本次输入为：", b[i],end='\t')
            print("运算符栈为：", operator.items, end='\t')
            print("运算数栈为：", Number.items, end='\n')

            break
    if(Number.is_empty() != True): print("\n\n运算结果为：", Number.peek())
    else: print("\n\n运算结果为：", float("".join(NumberTemp)))
'''a = input("输入表达式:" + "\n")
b = list(a)
b.append('#')
print(b)
OPTR = Stack()
Number = Stack()
operator = Stack()
operator.push('#')
i = 0
NumberTemp = []
while(True):
    print("运算符栈为：",operator.items,end='\t')
    if (b[i] == '*' or b[i] == '/' or b[i] == '+' or b[i] == '-' or b[i] == '(' or b[i] == ')' or b[i] == '#'):
        #print("nt",NumberTemp)
        if(NumberTemp != []):
            Nt = "".join(NumberTemp)
            Number.push(float(Nt))
            NumberTemp = []
        if(precede(operator.peek(),b[i]) == '<'):
            operator.push(b[i])
        elif(precede(operator.peek(),b[i]) == '='):
            x = operator.pop()
        elif(precede(operator.peek(),b[i]) == '>'):
            theta = operator.pop()
            x2 = Number.pop()
            x1 = Number.pop()
            print("运算",x1,theta,x2,end='\t')
            Number.push(operate(x1,theta,x2))
            i -= 1
    elif(isInt(b[i]) == 1 or b[i] == '.'):
        NumberTemp.append(b[i])
    else:
        b[i] = input("输入" + b[i] + "的值\n")
        NumberTemp.append(b[i])
    #if (b[i] != '#'):
    print("运算数栈为：", Number.items, end='\t')
    print("本次输入为：", b[i])
    i += 1
    #elif(b[i] == '#'):
    #
    if(operator.peek() == '#' and b[i] == '#'):
        print("运算符栈为：", operator.items, end='\t')
        print("运算数栈为：",Number.items,end='\t')
        print("本次输入为：",b[i])
        break
print("\n\n运算结果为：",Number.peek())'''
if __name__ == '__main__':
    s = input("输入表达式:" + "\n")
    jisuan(s)