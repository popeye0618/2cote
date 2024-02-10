#30
#내 풀이
#10의 배수여야 하고, 모든 자리수의 합이 3의 배수여야 함

n = input()

if '0' not in n:
  print(-1)
  exit(0)

t = 0
for i in n:
  t += int(i)

if t % 3 != 0:
  print(-1)
  exit(0)

else:
  n_list = list(n)
  n_list.sort(reverse = True)
  ans = ''.join(n_list)
  print(ans)
