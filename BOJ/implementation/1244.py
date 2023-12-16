#스위치 켜고 끄기(실버 4)
#내 풀이
#문제 요약을 해보면, 남학생은 받은 숫자의 배수의 스위치를 반대 상태로 만들고, 여학생은 받은 숫자를 중심으로 대칭이 아닐 때 까지 범위를 잡고, 그 범위의 스위치를 모두 바꾼다.

n = int(input())
sw = list(map(int, input().split()))
m = int(input())
student = []
for _ in range(m):
  row = list(map(int, input().split()))
  student.append(row)

for i in range(len(student)):
  if student[i][0] == 1: #남학생
    for j in range(1, (len(sw) // student[i][1]) + 1):
      sw[(student[i][1] * j) - 1] = 1 if sw[(student[i][1] * j) - 1] == 0 else 0
  else: #여학생
    t = student[i][1] - 1
    tlist = [-1, -1]
    bt, ft = t, t
    while True:
      bt -= 1
      ft += 1
      if bt < 0 or ft > len(sw) - 1:
        break
      else:
        if sw[bt] == sw[ft]:
          tlist[0], tlist[1] = bt, ft     
        else:
          break

    if tlist[0] == -1:
      sw[student[i][1] - 1] = 1 if sw[student[i][1] - 1] == 0 else 0
    else:
      for i in range(tlist[0], tlist[1] + 1):
        sw[i] = 1 if sw[i] == 0 else 0

for i in range(1, len(sw) + 1):
  print(sw[i-1], end=' ')
  if not i % 20:
    print()