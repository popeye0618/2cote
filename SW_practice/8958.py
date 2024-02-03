#OX퀴즈

t = int(input())

for _ in range(t):
  s = input()
  ans = 0
  pt = 0
  for i in s:
    if i == 'X':
      pt = 0
    else:
      pt += 1
      ans += pt
  print(ans)