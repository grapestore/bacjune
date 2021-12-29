import sys
sys.stdin = open('inputs.text')

vowel = {
  'a':0,
  'e':0,
  'i':0,
  'o':0,
  'u':0
}
result = {}

while True:
  que = sys.stdin.readline().rstrip()
  arr = list(map(str,que))

  if que == 'end':
    break

  result[que] = 0
  stack = []
  vowel_cnt = 0
  for x in arr:
    if x in vowel:
      vowel_cnt += 1
    if x != 'e' and x != 'o' and len(stack)>0 and stack[-1] == x:
      break
    if len(stack)>1:
      if x not in vowel:
        if stack[-1] not in vowel:
          if stack[-2] not in vowel:
            break
      else:
        if stack[-1] in vowel:
          if stack[-2] in vowel:
            break
    stack.append(x)
  else:
    if vowel_cnt>0:
      result[que] = 1

for key in result:
  temp = ''
  if result[key] == 0:
    temp = '<'+key+'> is not acceptable.'
    print(temp)
  else:
    temp = '<'+key+'> is acceptable.'
    print(temp)