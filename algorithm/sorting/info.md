1. 선택 정렬(시간복잡도: O(N^2))
  처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복

  array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
  for i in range(len(array)):
    min_index = i
    for j in range(i + 1, len(array)):
      if array[min_index] > array[j]:
        min_index = j
    array[i], array[min_index] = array[min_index], array[i]
  print(array)

2. 삽입 정렬(시간복잡도: O(N^2), 최선의 경우(거의 정렬된 경우) O(N))
  처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입(앞쪽에 있는 데이터는 정렬되어있다고 생각한다.)
  선택 정렬보다 구현 난이도가 높지만, 더 효율적이다.

  array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
  for i in range(1, len(array)):
    for j in range(i, 0, -1)
      if array[j] < arr[j - 1]:
        arr[j], arr[j - 1] = arr[j - 1], arr[j]
      else:
        break
  print(array)

3. 퀵 정렬(시간복잡도: O(NlogN) 최악의 경우(이미 정렬된 경우) O(N^2), 표준 라이브러리 사용 시 O(NlogN) 보장)
  기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
  가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터로 설정한다.
  왼쪽에서는 기준 데이터(피벗)보다 큰 데이터를 선택, 오른쪽은 작은 데이터를 선택 후 둘이 바꾼다.
  만약 피벗보다 큰 데이터와 작은 데이터의 위치가 서로 엇갈릴 경우 피벗과 작은 데이터의 위치를 서로 변경한다.

  array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

  def quick_sort(array, start, end):
    if start >= end: #원소가 1개인 경우 종료
      return
    pivot = start #피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
      #피벗보다 큰 데이터를 찾을 때까지 반복
      while left <= end and array[left] <= array[pivot]:
        left += 1
      #피벗보다 작은 데이터를 찾을 때까지 반복
      while right > start and array[right] >= array[pivot]:
        right -= 1
      if left > right: #엇갈렸다면 작은 데이터와 피벗을 교체
        array[right], array[pivot] = array[pivot], array[right]
      else: #엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        array[left], array[right] = array[right], array[left]
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
quick_sort(array, 0, len(array) - 1)
print(array)

파이썬의 장점을 살린 퀵 정렬 소스코드
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
  #리스트가 하나 이하의 원소만을 담고 있다면 종료
  if len(array) <= 1:
    return array
  pivot = array[0] #피벗은 첫 번째 원소
  tail = array[1:] #피벗을 제외한 리스트

  left_side = [x for x in tail if x <= pivot] #분할된 왼쪽 부분
  right_side = [x for x in tail if x > pivot] #분할된 오른쪽부분

  #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고 전체 리스트 반환
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)
print(quick_sort(array))


4. 계수 정렬
  특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 정렬 알고리즘
  계수 정렬은 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 가능
  데이터의 개수 N, 데이터(양수)중 최댓값이 K일 때 최악의 경우에도 수행시간 O(N + K)를 보장한다.
  작동방식은 0부터 값의 최대값까지 리스트를 만들고 몇 번 나오는지 count해서 0부터 순서대로 count만큼 출력하는 방식이다.
  * 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적으로 사용할 수 있다.ex)성적 (최악의 경우 데이터가 0과 999,999만 존재하는 꼴)

  #모든 원소의 값이 0보다 크거나 같다고 가정
  array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
  #모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
  count = [0] * (max(array) + 1)

  for i in range(len(array)):
    count[array[i]] += 1

  for i in range(len(count)):
    for j in range(count[i]):
      print(i, end = ' ')

