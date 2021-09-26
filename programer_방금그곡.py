import sys


m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
result = []
for music in musicinfos:
  start,end,title,mus = music.split(',')
  time = int(end[3:5]) - int(start[3:5])
  init_time = time
  lens_mus = len(mus)
  remains = lens_mus
  temp = ''

  while time > 0:
    if time >= lens_mus:
      temp += mus[:lens_mus]
    else:
      temp += mus[:time]
    time -= lens_mus

  if m in temp:
    index = temp.find(m)
    if temp[index+len(m)] != '#':
      result.append([title,init_time])

result.sort(key=lambda x: -x[1])
if len(result)>0:
  print(result[0][0])
else:
  print('(None)')
