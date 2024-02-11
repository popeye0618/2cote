# 수 이어쓰기 2
# 1~9 까지는 1자리
# 10에서 99까지는 2자리
# 100부터 999까지는 3자리
# 9, 90, 900

# n이 몇 자리수인지 알아내는게 먼저
# cnt = 1으로 두고 10씩 곱하면서 cnt보다 큰지 확인
# 몇 자리수인지 알아냈으면 그 수의 총 길이는 9 * (10 ** i) * (i + 1)
# 그다음 k가 몇 번째 수인지 알아내야 함
# 따라서 현재 자리수의 시작지점으로부터 몇 번째 수인지 k // 자리수를 더함
# 그럼 k가 들어있는 수를 알 수 있다.
# 그다음 k % 자리수를 하면 이 값이 k가 들어있는 수에서 몇 번째인지 알 수 있다.

n, k = map(int, input().split())
length = len(str(n))

tmp = 0
for i in range(1, length):
  tmp += 9 * (10**(i - 1)) * i

re = n - (10**(length - 1)) + 1
tmp += re * length

if tmp < k:
  print(-1)
else:
  k -= 1
  for i in range(1, length + 1):
    if k < 9 * (10**(i - 1)) * i:
      num = (10**(i - 1)) + k // i
      if num > n:
        print(-1)
      else:
        print(str(num)[k % i])
      break
    k -= 9 * (10**(i - 1)) * i
