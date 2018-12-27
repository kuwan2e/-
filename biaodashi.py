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
    if(o == '/'): return b/a
    if(o == '+'): return a+b

a = input("输入表达式:")
b = list(a)
b.insert(0,'(')
b.append(')')
print(b)
OPTR = Stack()
Number = Stack()
operator = Stack()
i = 0
while(i < len(b)):
    NumberTemp = []
    if(b[i] == ')'):
        while(operator.peek() != '('):
            Number.push(operate(Number.pop(), operator.pop(), Number.pop()))
        operator.pop()
        #Number.push(operate(Number.pop(),operator.pop(),Number.pop()))

        #print(Number.peek())
    else:
        if(b[i] == '*' or b[i] == '/' or b[i] == '+' or b[i] == '-' or b[i] == '('):
            operator.push(b[i])

        else:
            while (b[i] != '*' and b[i] != '/' and b[i] != '+' and b[i] != '-' and b[i] != '(' and b[i] != ')'):
                NumberTemp.append(b[i])
                i += 1
                #print(NumberTemp)
            Nt = "".join(NumberTemp)
            Number.push(float(Nt))
            i-=1

            #print("运算符栈为：" + operator.peek())
            #print("运算数栈为：" , Number.peek())
            if (operator.peek() == '*' or operator.peek() == '/'):
                Number.push(operate(Number.pop(), operator.pop(), Number.pop()))
            elif (operator.peek() == '-'):
                Number.push(-Number.pop())
                operator.pop()
                operator.push('+')
    i+=1

print(Number.peek())