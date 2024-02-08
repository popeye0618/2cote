#삼각형 만들기
#내 풀이
#우선 삼각형 만들려면 a + b > c 를 만족해야함(c가 가장 긴 길이)

n = int(input())
arr = []
for _ in range(n):
  arr.append(int(input()))

arr.sort(reverse = True)
flag = False
for i in range(n - 2):
  if arr[i] < arr[i + 1] + arr[i + 2]:
    print(arr[i] + arr[i + 1] + arr[i + 2])
    flag = True
    break
if not flag:
  print(-1)