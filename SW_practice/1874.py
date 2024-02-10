#스택 수열

n = int(input())
arr = []
for _ in range(n):
  arr.append(int(input()))
t = arr[:]
stack = []
ans = []
tmp = []
ptr = 1
while ptr <= n:
  if stack and stack[-1] == arr[0]:
    tmp.append(stack.pop())
    arr.pop(0)
    ans.append('-')
    continue
  else:
    stack.append(ptr)
    ans.append('+')
    ptr += 1
while stack:
  tmp.append(stack.pop())
  ans.append('-')
  
if t == tmp:
  for i in ans:
    print(i)
else:
  print('NO')