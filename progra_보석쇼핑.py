import sys
sys.stdin = open('inputs.text')


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
indivi_gem = []
for count in gems:
  if count not in indivi_gem:
    indivi_gem.append(count)
length = []
if len(indivi_gem)==1:
  answer = [1,1]
  print(answer)
  exit()

for i in range(len(gems)-len(indivi_gem)+1):
  dp = []
  dp.append(gems[i])
  for j in range(i+1,len(gems)):
    if gems[j] not in dp:
      dp.append(gems[j])
    if len(dp) == len(indivi_gem):
      temp = j-i
      length.append([j-i,i+1,j+1])
      break
  if temp == len(indivi_gem):
    break
    
length = sorted(length, key=lambda x : (x[0], x[1]))
answer = [length[0][1],length[0][2]]
print(answer)