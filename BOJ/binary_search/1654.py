#랜선 자르기(실버 2)
#내 풀이
#문제 범위만 봐도 이분탐색 문제
#랜선의 총 합을 n으로 나눈 값을 end값으로 잡고 이분탐색 시작
#이 값이 랜선의 최대 길이
#현재 mid값으로 랜선을 나눴을 때, n개 이상이 나온다면 start를 mid + 1로 만듦
#따라서 mid값이 커지고, 이 mid 값을 저장해 놓는다.
#n개가 안나오면 end를 줄여서 mid값을 낮춰 n개 이상이 나오도록 함
#반복문이 끝나면 저장한 result값 출력

k, n = map(int, input().split())
arr = []
for _ in range(k):
  arr.append(int(input()))

start = 1
end = sum(arr) // n

result = 0
while start <= end:
  mid = (start + end) // 2
  total = 0
  
  for line in arr:
    total += line // mid
  if total >= n:
    result = mid
    start = mid + 1
  else:
    end = mid - 1
    
print(result)