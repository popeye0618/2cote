이진 탐색 알고리즘

순차 탐색: 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인하는 방법
이진 탐색: 정렬되어 있는 리스트에서 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 방법
(이진 탐색은 시작점, 끝점, 중간점을 이용하여 탐색 범위를 설정한다.)

이진 탐색 동작 예시
정렬된 10개의 데이터 중 값이 4인 원소를 찾는다.
0 2 4 6 8 10 12 14 16 18
step 1) 시작점: 0, 끝점: 9, 중간점: 4 (소수점 이하 제거((0 + 9) / 2 -> 4))
찾고자 하는 값과 중간점의 값을 비교해서 끝점을 옮긴다.
step 2) 시작점: 0, 끝점: 3, 중간점: 1
step 3) 시작점: 2, 끝점: 3, 중간점: 2
중간점과 찾고자 하는 값이 같기 때문에 탐색 종료

시간복잡도
단계마다 탐색 범위를 2로 나누는 것과 동일하므로 log2 N에 비례한다.(O(log N))

재귀적 구현
def binary_search(array, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  #찾은 경우 중간점 인덱스 반환
  if array[mid] == target:
    return mid
  #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
  elif array[mid] > target:
    return binary_search(array, target, start, mid - 1)
  #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
  else:
    return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
  print('원소가 존재하지 않음')
else:
  print(result + 1)

반복문 구현
def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
      return mid
    #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  return None

파이썬 이진 탐색 라이브러리
bisect_left(a, x) : 정렬 된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
bisect_right(a, x) : 정렬 된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

이를 이용해서 값이 특정 범위에 속하는 데이터의 개수를 구할 때
bisect_right - bisect_left를 해주면 된다.

파라메트릭 서치(Parametric Search)
  최적화 문제를 결정 문제(yes or no)로 바꾸어 해결하는 기법
    ex) 특정한 조건을 만족하는 가장 알맞은 값을 빠르게 찾는 최적화 문제
  일반적으로 코딩테스트에서 파라메트릭 서치 문제는 이진탐색을 이용하여 해결할 수 있다.