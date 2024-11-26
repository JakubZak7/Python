import queue

def brackets_ok(expression):
    stack = queue.LifoQueue()
    brackets_map = {')': '(', ']': '[', '}': '{'}
    opening_brackets = brackets_map.values()
    closing_brackets = brackets_map.keys()
    
    for char in expression:
        if char in opening_brackets:
            stack.put(char)
        elif char in closing_brackets:
            if stack.empty() or stack.get() != brackets_map[char]:
                return False
    
    return stack.empty()

# Test the function
expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

if brackets_ok(expression1):
    print(f"Expression 1: {expression1} has correct brackets.")
else:
    print(f"Expression 1: {expression1} has incorrect brackets.")

if brackets_ok(expression2):
    print(f"Expression 2: {expression2} has correct brackets.")
else:
    print(f"Expression 2: {expression2} has incorrect brackets.")

if brackets_ok(expression3):
    print(f"Expression 3: {expression3} has correct brackets.")
else:
    print(f"Expression 3: {expression3} has incorrect brackets.")
