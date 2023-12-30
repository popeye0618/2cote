#게임(실버 3)
#내 풀이
#이분 탐색을 수행하며 승률이 변하면 스탑
#최소 몇판이므로 승률이 변하기 전에는 left를 바꾸고, 바뀌고 나서부터는 right를 바꾼다.
#이분 탐색을 진행하면서 mid만큼 게임을 더 했다는 뜻이고, 승률이 바뀌면 right를 줄여서 더 작은 값을 찾아본다.
#무조건 승률은 올라갈 수 밖에 없으므로 승률이 z보다 커진다는 것이 승률이 변하는 것이다.

x, y = map(int, input().split())
z = (y * 100) // x

def binary_search(z, x, y):
  if z >= 99:
    return -1
  left = 1
  right = x
  ans = 0
  while left <= right:
    mid = (left + right) // 2
    if ((y + mid) * 100) // (x + mid) > z:
      ans = mid
      right = mid - 1
    else:
      left = mid + 1
  return ans

print(binary_search(z, x, y))