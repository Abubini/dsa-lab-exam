letter = input("enter text: ")
stack = []

def check_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)


def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"
    return stack.pop()




for i in letter:
    push(stack,i)


def stack_reverse(stack):
    temp = []
    for i in range(len(stack)):
        temp.append(pop(stack))
    return temp
result = stack_reverse(stack)

for i in range(len(result)):
    print(result[i], end="")
