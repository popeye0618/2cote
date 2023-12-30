#두 용액(골드 5)
#내 풀이
#음수와 양수를 분리하고 bisect를 이용해서 left로 0과의 거리 비교

#피드백
#우선 내 방식은 접근 자체가 틀렸다. 음수와 양수가 동시에 입력되도 양수에서만 답이 나올 수도 있는 것
#검색해보니 이 문제는 투포인터라는 방식으로 문제를 해결한다
#양쪽 맨 끝을 잡고 이 둘을 더해서 절대값이 더 작으면 저장
#계속해서 더한 값이 음수이면 left + 1 양수이면 right - 1을 해주면서 반복

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = n - 1
min_value = abs(arr[left] + arr[right])
ans = [arr[left], arr[right]]

while left < right:
  sum = arr[left] + arr[right]
  if abs(sum) < min_value:
    min_value = abs(sum)
    ans = [arr[left], arr[right]]
    if sum == 0:
      break
      
  if sum < 0:
    left += 1
  else:
    right -= 1

print(' '.join(map(str, ans)))