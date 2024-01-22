#공유기 설치(골드 4)
#내 풀이
#이분 탐색 문제는 항상 어떤 부분을 이분 탐색 할 지가 고민된다.
#근데 풀었던 문제들은 항상 구해야 하는 값을 mid로 구할 수 있게끔 되어있었다.
#따라서 인접한 최대의 거리를 구하니까 거리를 이분탐색 해보자
#설치한 집과 설치 안한 집 사이의 거리가 mid보다 크다면 공유기를 설치해준다.
#공유기의 개수가 많으면, 거리가 짧았다는 소리니까 left를 움직인다.

n, c = map(int, input().split())
house = []
for _ in range(n):
  house.append(int(input()))

house.sort()
left = 1
right = house[-1] - house[0]

result = 0
if n == 2:
  result = right
else:
  while left <= right:
    mid = (left + right) // 2
    cnt = 1
  
    now = house[0]
    for i in house:
      if i - now >= mid:
        cnt += 1
        now = i
  
    if cnt >= c:
      result = mid
      left = mid + 1
    else:
      right = mid - 1

print(result)