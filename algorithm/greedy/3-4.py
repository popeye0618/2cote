#1이 될 때까지
#어떤 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행
#1. N - 1
#2. N / K 단, 이 연산은 N이 K로 나누어 떨어질 때만 선택가능
#N과 K가 주어지면 N이 1이 될 때까지 과정을 수행해야 하는 최소 횟수를 출력

#내 풀이
#N-1을 계속 하다가 N이 K로 나누어 떨어지면 나누는 과정을 반복
#정당성 분석
#K가 2 이상이기만 하면 1씩 빼는 것 보다 반드시 N을 빠르게 줄일 수 있다. 또한 N은 항상 1에 도달하게 된다.

#피드백
#처음에 수학적으로 계산해서 반복의 횟수를 줄일 수 있다. 나누는 횟수만 반복문으로 세줄 수 있다.

#n, k = map(int, input().split())
#count = 0

#while n != 1:
#  if n % k == 0:
#    n //= k
#  else:
#    n -= 1
#  count += 1
#
#print(count)

#피드백 코드
n, k = map(int, input().split())
count = 0

while True:
  #이 과정으로 -1연산을 계속 수행하지 않고 한 번에 계산 가능
  target = (n // k) * k
  count += (n - target)
  n = target

  if n < k:
    break
  count += 1
  n //= k

count += (n - 1)
print(count)