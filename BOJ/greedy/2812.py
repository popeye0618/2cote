#크게 만들기(골드 3)
#내 풀이
#n자리 숫자에서 k만큼 지워서 얻을 수 있는 가장 큰 수를 얻으려면
#맨 앞자리부터 카운트 시작해서 본인보다 큰 수가 나오면 그 만큼 지운다.
#반례로 98765 이렇게 나올 수 있다.
#반례의 경우 총 지운 숫자의 개수가 k가 안될경우, 뒤에서부터 남은 k만큼 지운다.
#그리고 결국 자리수는 정해져있으므로, 처음 자리수 정하기 전까지는 다 지운다.

n, k = map(int, input().split())
num = input()

ans = []
same = 0
flag = -1
delete = 0

for i in range(len(num) - 1):
  now = int(num[i])
  next = int(num[i + 1])

  if delete == k:
    break
  if now > next:
    if same > 0:
      for _ in range(same):
        ans.append(now)
    delete += i - (flag + 1) - same
    flag = i
    ans.append(now)
  elif now == next:
    same += 1
  else:
    if same > 0:
      same = 0

rest = list(map(int, num[flag + 1 :]))
print(ans, rest, delete)

if not ans:
  rest.reverse()
  for _ in range(k):
    rest.pop()
  rest.reverse()
  ans += rest
  
else:
  if len(ans) > n - k:
    for _ in range(len(ans) - (n - k)):
      ans.pop()
  elif len(ans) == n - k:
    cnt = 0
    arr = []
    for i in range(len(ans) - 1):
      if cnt < len(rest) and ans[i] < ans[i + 1]:
          arr.append(i)
          cnt += 1
    for i in arr:
      ans.pop(i)
    for i in range(cnt):
      ans.append(rest[i])
  else:
    cnt = 0
    arr = []
    for i in range(len(ans) - 1):
      if cnt < len(rest) and ans[i] < ans[i + 1]:
          arr.append(i)
          cnt += 1
    for i in arr:
      ans.pop(i)
    for _ in range(cnt):
      ans.append(rest[0])
      rest.pop(0)
      
    t = len(rest) - ((n - k) - len(ans))
    for i in range(t, len(rest)):
      ans.append(rest[i])
    
print(''.join(map(str, ans)))