#신입사원(실버 1)
#내 풀이
#앞의 점수를 정렬시켜놓고 뒤에 점수를 비교하면 뒤로 갈수록 반드시 첫 번째 점수는
#다른 지원자보다 떨어지므로 두 번째 점수는 높아야한다.
#현재 두 번째 점수가 가장 높았던걸 기록하고, 비교하며 더 높은 등수가 들어오면
#결과 +1하고 기록한 점수를 갱신한다.

t = int(input())

for _ in range(t):
  n = int(input())
  score = []
  for _ in range(n):
    a, b = map(int, input().split())
    score.append((a, b))

  score.sort()

  result = 1
  min_rank = score[0][1]
  for i in range(n):
    if score[i][1] < min_rank:
      result += 1
      min_rank = score[i][1]

  print(result)