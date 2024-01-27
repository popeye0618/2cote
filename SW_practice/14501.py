#퇴사
#내 풀이
#역순으로 탐색하면서 우선 현재 날짜 + t가 퇴사일이 넘어가는지 확인
#넘어간다면 상담을 진행할 수 없으므로 앞의 값 그대로 가져옴
#넘어가지 않는다면 상담 진행 가능이므로 상담을 안했을 때와, 오늘 상담을 했을 때를 비교
#더 큰 값을 dp테이블에 저장

n = int(input())
t = []
p = []
for _ in range(n):
  a, b = map(int, input().split())
  t.append(a)
  p.append(b)

dp = [0] * (n + 1)

for i in range(n - 1, -1, -1):
  if i + t[i] <= n:
    dp[i] = max(dp[i + 1], dp[i + t[i]] + p[i])
  else:
    dp[i] = dp[i + 1]

print(dp[0])