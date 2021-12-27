import sys

t1 = [[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
t2 = [[1,2],[-1,-1],[-1,-1]]

# 0: 자식 x, 1: 왼ㅉ고만, 2:우측만 3: 둘다

def t2_check(start):
  shape = -1
  check_left, check_right = False, False
  for left, right in t2[start]:
    if left != -1:
      check_left = True
    if right != -1:
      check_right = True

  if check_left == True and check_right==True:
    shape = 3
  elif check_left == False and check_right==True:
    shape = 2
  elif check_left == True and check_right==False:
    shape = 1
  else:
    shape = 0

  return shape

t2_shape = t2_check(0)
print(t2_shape)