import sys
get_data = sys.stdin.readline().strip()
print(get_data)
stack = []

def handle_input(s):
    print(s)
    if s == '(' or '[':
        stack.append(s)


for i in get_data:
    handle_input(i)

print(stack)