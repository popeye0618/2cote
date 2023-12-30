#기타 레슨(실버 1)
#내 풀이
#이진 탐색을 하면서 왼쪽, 오른쪽으로 분할될 때 더 분할된 애들의 합이 작은 걸 기록하고, 큰 쪽으로 시작점을 옮긴다.
#이진 탐색을 M - 1번 수행한다.

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def binary_search(arr, start, end):
  while start <= end:
    
  