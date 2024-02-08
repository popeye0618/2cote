#부분수열의 합
#재귀를 통해 모든 경우의 수를 다 해봄
#현재 값이 포함된 경우, 현재 값이 포함되지 않는 경우

n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

def dfs(idx, total):
  global ans
  if idx == n:
    return
  if total + arr[idx] == s:
    ans += 1

  dfs(idx + 1, total + arr[idx])
  dfs(idx + 1, total)

dfs(0, 0)
print(ans)