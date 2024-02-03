#N과 M(3)

def gen_seq(n, m, now):
  if len(now) == m:
    print(' '.join(map(str, now)))
    return

  for i in range(1, n + 1):
    now.append(i)
    gen_seq(n, m, now)
    now.pop()

n, m = map(int, input().split())
temp = []
gen_seq(n, m, temp)