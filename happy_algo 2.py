import sys
from collections import deque

data = dict({
  'user1':[1,'man1','woman1'],
  'user2':[1,'man2','woman1'],
  'user3':[1,'man3','woman1'],
  'user4':[0,'woman1',"man2"],
  'user5':[0,'woman2','man2'],
  'user6':[0,'woman3','man2']
})

man_list = []
man_choice = {}
woman_list = []
woman_choice = {}
marrige_check = {}
gender = {}

for i in data:
  # print(data[i])
  if data[i][0] == 1:
    man_list.append(data[i][1])
    man_choice[data[i][1]] = data[i][2]
  else:
    woman_list.append(data[i][1])
    woman_choice[data[i][1]] = data[i][2]
  marrige_check[data[i][1]] = False
  gender[data[i][1]] = data[i][0]

result = []
crying = []
for i in man_list:
  temp = []
  for j in woman_list:
    if woman_choice[j] == i and marrige_check[i] == False and marrige_check[j] == False:
      temp.append(j)
  
  if man_choice[i] in temp:
    result.append([i, man_choice[i]])
    marrige_check[i] = True
    marrige_check[man_choice[i]] = True
  elif len(temp)>0 and man_choice[i] not in temp:
    man_choice[i] = temp[0]
  elif len(temp) == 0 and marrige_check[i] == False:
    crying.append(i)


for i in woman_list:
  temp = []
  for j in man_list:
    if man_choice[j] == i and marrige_check[i] == False and marrige_check[j] == False:
      temp.append(j)

  if woman_choice[i] in temp:
    result.append([i, woman_choice[i]])
    marrige_check[i] = True
    marrige_check[woman_choice[i]] = True
  elif len(temp)>0 and woman_choice[i] not in temp:
    woman_choice[i] = temp[0]
    if(man_choice[temp[0]] == i):
      
      result.append([i, man_choice[temp[0]]])
  elif len(temp) == 0 and marrige_check[i] == False:
    crying.append(i)

crying_man = []
crying_woman = []
woman_count = 0
man_count = 0
while crying:
  print(crying)
  human = crying.pop()
  
  if gender[human] == 1:
    crying_man.append(human)
  else:
    crying_woman.append(human)

  if len(crying_man)>0 and len(crying_woman)>0:
    result.append([crying_man.pop(), crying_woman.pop()])
    

print(result)