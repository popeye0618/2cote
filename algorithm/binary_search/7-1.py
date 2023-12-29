#떡볶이 떡 만들기
#절단기에 높이(H)를 지정하면 줄지어진 떡을 한 번에 절단한다. 높이가 H보다 긴 떡은 위 부분이 잘리고, 낮은 떡은 잘리지 않는다.
#손님은 잘린 떡의 길이 만큼 가져간다.
#손님이 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구해라

#문제 해결 아이디어
#적절한 높이를 찾을 때까지 이진 탐색을 수행하여 높이 h를 반복해서 조정한다.
#현재 이 높이로 자르면 조건을 만족할 수 있는가? 를 확인한 뒤에 조건의 만족 여부(yes or no)에 따라서 탐색 범위를 좁혀서 해결
#절단기의 높이가 10억까지이므로 이렇게 큰 탐색 범위를 보면 이진탐색을 떠올려야 한다.

n, m = map(int, input().split())
array = list(map(int, input().split()))

#이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

#이진 탐색 수행(반복적)
result = 0
while start <= end:
  total = 0
  mid = (start + end) // 2
  for x in array:
    #잘랐을 때의 떡의 양 계산
    if x > mid:
      total += x - mid
  #떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
  if total < m:
    end = mid - 1
  #떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
  else:
    result = mid #최대한 덜 잘랐을 때가 정답이므로 여기에서 result에 기록
    start = mid + 1

print(result)