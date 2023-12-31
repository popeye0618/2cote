다이나믹 프로그래밍
메모리를 적절히 사용하여 수행시간 효율성을 비약적으로 향상시키는 방법
이미 계산 된 결과(작은 문제)는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 한다
일반적으로 탑다운, 바텀업 방식으로 구현한다

다이나믹 프로그래밍은 문제가 다음의 조건을 만족할 때 사용할 수 있다
1. 최적 부분 구조
  큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있다.
2. 중복되는 부분 문제
  동일한 작은 문제를 반복적으로 해결해야한다.

메모이제이션(탑다운 방식에서 사용) = 캐싱
  한 번 계산한 결과를 메모리 공간에 메모하는 기법
  같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져온다.

바텀 업 방식은 보통 반복문으로 구현한다.
dp의 전형적인 형태는 바텀 업 방식이다.

탑다운 방식 피보나치 수열

dp = [0] * 100
def fibo(x):
  #종료 조건(1 혹은 2일 때 1을 반환)
  if x == 1 or x == 2:
    return 1
  #이미 계산한 적이 있는 문제라면 그대로 반환
  if dp[x] != 0:
    return dp[x]
  #아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
  dp[x] = fibo(x - 1) + fibo(x - 2)
  return dp[x]
print(fibo(99))

바텀업 방식 피보나치 수열

dp = [0] * 100
dp[1] == 1
dp[2] == 1
n = 99

for i in range(3, n + 1):
  dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])

dp와 분할 정복의 차이
  우선 둘 다 최적 부분 구조를 가질 때 사용할 수 있다.
  차이점은 부분 문제의 중복인데
  dp문제에서는 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복된다
  하지만 분할 정복 문제에서는 동일한 부분 문제가 반복적으로 계산되지 않는다.

dp문제에 접근하는 방법
  - 주어진 문제가 dp유형임을 파악하는 것이 중요하다.
  - 가장 먼저 그리디, 구현, 완전탐색 등의 아이디어로 문제를 해결할 수 있는지 검토한다.
  - 다른 알고리즘으로 풀이 방법이 떠오르지 않으면 dp를 고려한다.  
  - 일단 재귀함수로 비효율적인 완전탐색 프로그램을 작성한 뒤에 (탑다운) 작은 문제에서 구한 답이
    큰 문제에서 그대로 사용될 수 있으면, 코드를 개선하는 방법을 사용할 수 있다.