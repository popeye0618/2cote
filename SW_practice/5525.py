#IOIOI
#내 풀이
#문자열에 IOI가 연속으로 있을 때, 그 길이와 개수를 센다.
#연속으로 있다면 길이를 1 증가시키고, 포인터를 2 증가시켜 계속해서 확인한다.
#길이가 n을 만족하면 앞의 IO를 없애고(길이 -1)계속 이어간다.
#패턴이 끊겼다면 포인터를 1만 증가시킨다.

n = int(input())
k = int(input())
s = input()

cnt = 0
leng = 0

i = 0
while i < k - 2:
  if s[i] == 'I' and s[i + 1] == 'O' and s[i + 2] == 'I':
    leng += 1
    if leng == n:
      leng -= 1
      cnt += 1
    i += 2
  else:
    leng = 0
    i += 1

print(cnt)