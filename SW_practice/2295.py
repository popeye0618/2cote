#세 수의 합
#내 풀이
#두 수의 합을 다 구해놓고, 값 하나씩 잡아서 비교
#값 두 개를 잡고 뺏을 때, 그 값이 arr_sum에 들어있는 값이면 조건 만족
#뺀 값 + 두 수의 합 = 원래 값

n = int(input())
arr = []
for _ in range(n):
  arr.append(int(input()))

arr.sort()
arr_sum = set()
for i in range(n):
  for j in range(n):
    arr_sum.add(arr[i] + arr[j])

answer = 0
for i in arr:
  for j in arr:
    if i - j in arr_sum:
      answer = max(answer, i)
      break
      
print(answer)