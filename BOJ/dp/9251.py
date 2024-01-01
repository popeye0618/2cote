#LCS(골드 5)
#내 풀이
#최장 공통 부분수열 문제
#dp의 값은 i번째 인덱스에서의 최장 공통 부분수열의 길이이다.
#두 값이 같다면 dp[i - 1][j - 1] + 1이고 두 값이 다르다면 부분수열의 길이가 증가할 순 없으므로
#dp[i - 1][j]와 dp[i][j - 1]을 비교해서 큰 값으로 이어간다.

a = input()
b = input()

dp = [[0 for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]

for i in range(len(b) + 1):
  for j in range(len(a) + 1):
    if i == 0 or j == 0:
      dp[i][j] = 0
    elif a[j - 1] == b[i - 1]:
      dp[i][j] = dp[i - 1][j - 1] + 1
    else:
      dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(b)][len(a)])