#신입 사원(실버 1)
#내 풀이
#입력을 받고 정렬을 한다. 서류 순으로 정렬 후 면접 점수를 비교. 오른쪽으로 가는 것은 서류는 반드시 누군가보다 낮다는 의미이고, 면접 점수는 가장 높은 순위로 갱신하면서 이 값보다 작다면 탈락, 값보다 크다면 +1하고, 높은 순위를 갱신하는 방식으로 진행한다.

t = int(input())

for _ in range(t):
  n = int(input())
  score = []
  for _ in range(n):
    row = list(map(int, input().split()))
    score.append(row)
  score = sorted(score, key = lambda x:x[0])

  high_rank = score[0][1]
  result = 0
  for i in range(n):
    if score[i][1] <= high_rank:
      result += 1
      high_rank = score[i][1]
  print(result)
