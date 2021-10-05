

gems = ["XYZ", "XYZ", "XYZ"]
indivi_gem = dict()
temp = set(gems)
for count in temp:
  indivi_gem[count] = 0
length = []

if len(indivi_gem)==1:
  answer = [1,1]
  print(answer)
  exit()

count = 0
start = 0
end = 0
diff = 1000001
for i in gems:
  end += 1
  indivi_gem[i] += 1

  if 0 not in indivi_gem.values():
    while indivi_gem[gems[start]] > 1:
      indivi_gem[gems[start]] -= 1
      start+=1
    if end-start < diff:
      diff = end-start
      length = [[diff,start+1,end]]

answer = [length[0][1],length[0][2]]
print(answer)