#세수의 합(골드 4)
#내 풀이
#투 포인터 문제
#두 수의 합을 계산해 놓고, 두 값을 잡는다.
#이 두 값을 뺀 값이 두 수의 합이 있는 집합에 존재하면
#뺄 때 사용한 큰 값이 최대 값이므로 저장된 값과 비교 후 저장

n = int(input())
arr = []
for _ in range(n):
  arr.append(int(input()))

arr.sort()
sum_arr = set()

for i in range(n):
  for j in range(n):
    sum_arr.add(arr[i] + arr[j])

result = 0

for c in arr:
  for a in arr:
    if c - a in sum_arr:
      result = max(result, c)
      break

print(result)