#수 묶기(골드 4)
#내 풀이 (1트 성공)
#양수와 음수로 나누고 음수는 0포함, 오름차순, 양수는 내림차순으로 정렬, 양수는 1 제외
#각 리스트의 가장 작은 수는 맨 뒤에 존재하므로, 리스트의 길이가 홀수인 경우 어차피 못묶일 것이기 때문에 미리 더해주고 리스트를 슬라이싱해서 짝수 크기로 만든다.
#1의 개수를 먼저 결과에 더해준다.
#그 후 각 배열의 i번쨰와 i+1번째를 무조건 곱해서 결과에 더한다.
#정당성 분석
#음수끼리 곱하는 것은 음수가 짝수개인 경우 양수가 되므로 최대의 결과값을 얻을 수 있고, 0을 음수 리스트에 포함하는 이유는 양수는 0과 만나면 무조건 더하기 연산이지만, 음수는 자기보다 작은 음수와 곱해지는게 아닌 이상 0과 곱하는게 최대 값을 만들기 유리하기 때문이다
#1의 개수를 더해주는 이유는 1은 뭐랑 곱해도 다 자기자신이기 때문에 더해주는게 무조건 커지기 때문
#양수를 내림차순으로 한 이유는 큰 값부터 묶기 위해서


n = int(input())
arr = []
for _ in range(n):
  arr.append(int(input()))
arr.sort()

natural = []
negative = []
result = 0

for i in arr:
  if i <= 0:
    negative.append(i)
  elif i > 1:
    natural.append(i)
  else:
    result += 1

natural.sort(reverse=True)

if len(negative) % 2 != 0:
  result += negative[-1]
  negative = negative[:-1]
for i in range(0, len(negative)-1, 2):
  result += negative[i] * negative[i+1]

if len(natural) % 2 != 0:
  result += natural[-1]
  natural = natural[:-1]
for i in range(0, len(natural)-1, 2):
  result += natural[i] * natural[i+1]

print(result)