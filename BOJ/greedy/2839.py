#설탕 배달 (실버4)
#내 풀이 (1트 성공)
#3kg와 5kg 중 5kg 위주로 담아야 결과가 반드시 적어지므로 5로 나누어 지기 전까지는 3을 빼고, 나누어 지면 5로 나눈다. 나눈 나머지가 3이면 나누고 3이 아니면 -1을 출력한다.

n = int(input())
result = 0

while True:
  if n % 5 == 0:
    result += n // 5
    n %= 5

  if n < 5:
    break
  n -= 3
  result += 1

if n == 3:
  n -= 3
  result += 1

if n == 0:
  print(result)
else:
  print(-1)
