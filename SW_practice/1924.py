#2007년
#구현

x, y = map(int, input().split())
a = [1, 3, 5, 7, 8, 10, 12]
b = [4, 6, 9, 11]
ans = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
day = -1
for i in range(1, x + 1):
  if i == x:
    for _ in range(1, y + 1):
      day += 1
  elif i == 2:
    day += 28
  elif i in a:
    day += 31
  elif i in b:
    day += 30

day %= 7
print(ans[day])