#왕실의 나이트
#왕실 정원은 8*8 좌표평면이다. 특정한 한 칸에 나이트가 서있다. 나이트는 L자로만 움직일 수 있으며, 정원 밖으로는 나갈 수 없다.
#1. 수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
#2. 수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기
#나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램 작성
#행의 위치는 1~8, 열의 위치는 a~h

start = input()
x = int(ord(start[0])) - int(ord('a')) + 1
y = int(start[1])
cnt = 8

dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]

for i in range(8):
  nx = x + dx[i]
  ny = y + dy[i]
  if nx < 1 or ny < 1 or nx > 8 or ny > 8:
    cnt -= 1
print(cnt)