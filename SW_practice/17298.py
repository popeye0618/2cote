#오큰수(골드 4)
#내 풀이
#리스트를 탐색하면서 오큰수를 찾는다.
#스택에는 오큰수를 아직 찾지 못한 인덱스들을 넣는다.
#리스트의 인덱스를 이동할 때마다 스택에 있는 애들을 현재 수와 비교해본다.
#순서상 스택에 가장 위에 있는 수가 제일 작은 수라는 것이 보장되어있다.

n = int(input())
nums = list(map(int, input().split()))
answer = [-1] * n
stack = []

for i in range(n):
  while stack and nums[stack[-1]] < nums[i]:
    answer[stack.pop()] = nums[i]
  stack.append(i)

print(' '.join(map(str, answer)))