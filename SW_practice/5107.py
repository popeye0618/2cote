#마니또(실버 1)
#내 풀이
#이 문제도 사이클 찾는 문제다

t = 1
while True:
  n = int(input())
  if n == 0:
    break

  arr = [set()]
  for _ in range(n):
    a, b = input().split()
    flag = False
    for i in range(len(arr)):
      if a in arr[i] or b in arr[i]:
        flag = True
        arr[i].add(a)
        arr[i].add(b)
    if not flag:
      new = set()
      new.add(a)
      new.add(b)
      arr.append(new)

  print(t, len(arr) - 1)
  t += 1