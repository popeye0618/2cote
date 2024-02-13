#해싱

r = 31
m = 1234567891

arr = [chr(x) for x in range(ord('a'), ord('z') + 1)]

n = int(input())
s = input()

answer = 0
for i in range(n):
  now = arr.index(s[i]) + 1
  answer += now * (r ** i) % m
  
print(answer % m)