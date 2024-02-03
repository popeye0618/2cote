#N과 M(1)
#내 풀이
#순열 출력인데 중복 허용 x

def permutation(n, m, now):
  if len(now) == m:
    print(' '.join(map(str, now)))
    return

  for i in range(1, n + 1):
    if i in now:
      continue
    now.append(i)
    permutation(n, m, now)
    now.pop()

n, m = map(int, input().split())
temp = []
permutation(n, m, temp)