#기타 레슨
#내 풀이
#start는 최대값, end는 총 합으로 두고 이분 탐색
#중요한점은 total의 초기 값은 1이라는 점이다.
#만약 0으로 시작한다면 마지막에 tmp + x가 mid보다 크지 않다면
#블루레이가 하나 덜 계산되기 때문이다.

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = max(arr)
end = sum(arr)

result = 0
while start <= end:
  mid = (start + end) // 2
  total = 1
  tmp = 0
  
  for x in arr:
    if tmp + x > mid:
      total += 1
      tmp = 0
    tmp += x

  if total <= m:
    result = mid
    end = mid - 1
  elif total > m:
    start = mid + 1

print(result)