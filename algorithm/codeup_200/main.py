#97번 문제
h, w = map(int, input().split())
n = int(input())
a = []
for _ in range(n):
  row = list(map(int, input().split()))
  a.append(row)
  
ans = [[0 for _ in range(w)] for _ in range(h)]

for i in range(n):
  if(a[i][1] == 0): #가로일 경우
    for j in range(a[i][0]):
      ans[a[i][2]-1][a[i][3]-1+j] = 1
  else:
    for j in range(a[i][0]):
      ans[a[i][2]-1+j][a[i][3]-1] = 1

for i in range(h):
  for j in range(w):
    print(ans[i][j], end=' ')
  print()