import sys
sys.stdin = open('inputs.text')

que = sys.stdin.readline().strip()
search = sys.stdin.readline().strip()
# while que:
#   temp = que
#   que = que.replace(search, '')
#   if(temp == que):
#     break

# if(len(que)==0):  
#   print('FRULA')
# else:
#   print(que)
    
stack = []
last_alpha = search[-1]
length_search = len(search)
for alphabet in que:
  stack.append(alphabet)
  if alphabet == last_alpha and "".join(stack[-length_search:])==search:
    del stack[-length_search:]

if len(stack) == 0:
  print('FRULA')
else:
  print("".join(stack))
