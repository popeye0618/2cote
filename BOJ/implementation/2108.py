#통계학 (실버3)
#내 풀이
#평균은 그냥 반올림, 중앙값은 정렬 후 n // 2 번째 값, 최빈값은 collections의 counter 사용, 범위는 큰 값 - 작은 값의 절댓값

#피드백
#처음 Counter을 써봤고, 이를 정렬하는 것도 연습해야 한다. lambda 함수 사용도 정렬할 때 많이 쓰이므로 익숙해지자

from collections import Counter

n = int(input())
arr = []
sum = 0
for _ in range(n):
  t = int(input())
  sum += t
  arr.append(t)

arr.sort()
counter = Counter(arr)
sorted_counter = sorted(counter.items(), key = lambda x : (-x[1], x[0]))

print(int(round(sum / n)))
print(arr[n // 2])
if n > 1:
  if sorted_counter[0][1] == sorted_counter[1][1]:
    print(sorted_counter[1][0])
  else:
    print(sorted_counter[0][0])
else:
  print(arr[0])
print(abs(arr[-1] - arr[0]))
