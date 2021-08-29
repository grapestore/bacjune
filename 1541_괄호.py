import sys
sys.stdin = open('inputs.text')
question = list(sys.stdin.readline().split('-'))
result = 0
init = 0
if '+' not in question[0]:
    temp = question.pop(0)
    init = int(temp)
else:
    temp = list(map(int,question[0].split('+')))
    question.pop(0)
    init = sum(temp)
for data in question:
    temp = list(map(int,data.split('+')))
    result += sum(temp)
print(init - result)    
