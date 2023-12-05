#주유소 (실버3)
#내 풀이
#가장 저렴한 곳에서 남은 거리 만큼 주유를 하면 되고, 가장 저렴한 곳까지 도착하기 전에는 가야 할 거리만큼만 주유한다. 리터 당 가격과 거리의 값 제한이 상당히 크다는 것을 주의(파이썬이라 신경안쓰고 해본다)
#피드백(1트 성공)
#가격이 나보다 낮은 곳이 나오기 전까지는 그 가격으로 구매하는 방식으로 짜야한다.

n = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))
result = 0

min_price = price[0]

for i in range(len(dis)):
  if min_price > price[i]:
    min_price = price[i]
  result += dis[i] * min_price

print(result)
  
    
    