#숫자 카드 게임
#여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
#N*M형태로 카드가 놓여있고, 행 하나를 선택해서 그 행 중 가장 작은 숫자 카드를 뽑을 수 있다.
#입력 조건: 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 각각 자연수로 주어진다.(1 <= N,M <= 100)
#둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1이상 10000 이하의 자연수이다.

n, m = map(int, input().split())
ans = 0

for _ in range(n):
  data = list(map(int, input().split()))
  min_value = min(data)
  ans = max(ans, min_value)

print(ans)
