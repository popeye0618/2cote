#N-Queen
#내 풀이
#퀸 n개가 서로 공격할 수 없는 경우를 찾는거니까 백트래킹으로 모든 경우의 수 시도
#그 상황에서 퀸은 상하좌우 모든 칸 갈 수 있는 말이니까 그 경우 비교
#최적화
#퀸을 놨으면 그 퀸의 가로, 세로, 대각의 줄에는 애초에 안놓도록 한다.
#퀸을 놓은 경우를 세로, 대각선 두 개로 된 세 개의 배열로 관리해서 방문 체크
#가로는 이미 cnt로 늘려주면서 놓기 때문에 검사할 필요 없음
#대각선 체크할 때는 x + y값이 대각선의 값과 같기 때문에 x + y로 검사
#부대각선은 x축을 뒤집으면 주대각선과 같이 비교 가능, 따라서 (n - 1) - x + y

def check(x, y):
  if visited_col[y] or visited_diag1[x + y] or visited_diag2[(n - 1) + x - y]:
    return False
  return True

def queen(cnt):
  global answer
  if cnt == n:
    answer += 1
    return
  for i in range(n):
    if check(cnt, i):
      visited_col[i] = True
      visited_diag1[cnt + i] = True
      visited_diag2[(n - 1) + cnt - i] = True
      queen(cnt + 1)
      visited_col[i] = False
      visited_diag1[cnt + i] = False
      visited_diag2[(n - 1) + cnt - i] = False

n = int(input())
graph = [[0] * n for _ in range(n)]
visited_col = [False] * n
visited_diag1 = [False] * (2 * n - 1)
visited_diag2 = [False] * (2 * n - 1)
answer = 0
queen(0)
print(answer)