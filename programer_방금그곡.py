import sys
from datetime import datetime, timedelta

MAPPER = {
        "C": "1",
        "C#": "2",
        "D": "3",
        "D#": "4",
        "E": "5",
        "F": "6",
        "F#": "7",
        "G": "8",
        "G#": "9",
        "A": "A",
        "A#": "B",
        "B": "C"
    }
CHAR_SH = ["C#", "D#", "F#", "G#", "A#"]
CGAR_NS = ["C", "D", "E", "F", "G", "A", "B"]

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]

def change(arr):
  for target in CHAR_SH:
    arr = arr.replace(target,MAPPER[target])
  for target in CGAR_NS:
    arr = arr.replace(target,MAPPER[target])
  return arr

m = change(m)

result = []
for music in musicinfos:
  start,end,title,mus = music.split(',')
  mus = change(mus)
  start_hour = int(start[:2])
  start_minutes = int(start[3:5])
  end_hour = int(end[:2])
  end_minutes = int(end[3:5])
  hour_cal = end_hour - start_hour
  minutes_cal = end_minutes - start_minutes
  time = minutes_cal + hour_cal*60
  

  temp = mus*(time//len(mus)) + mus[:(time%len(mus))]

  if m in temp:
    result.append([title,time,start_hour,start_minutes])

result.sort(key=lambda x: -x[1])
if len(result)>0:
  print(result[0][0])
else:
  print('(None)')
