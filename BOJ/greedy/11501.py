#주식(실버 2)
#내 풀이
#입력 받은 주식 값 리스트를 복사해서 크기순으로 내림차순 정렬을 해놓고, 오늘 값과 내일 값을 비교해서 오늘 값이 더 작으면 사고, 크면 사지 않는다. 그리고 크면 사지 않는다 이 과정을 실행 하기 전에 내림차순 정렬 해놓은 리스트를 보고 그 리스트의 포인터가 가리키는 값보다 작으면 산다. 내일 값을 비교할 때 내림차순 정렬 리스트랑도 비교해서 같은 값이면 내림차순 리스트 포인터를 한칸 옮긴다.(그 다음 큰 값도 알아야하기 때문에)

#피드백
#솔직히 반례도 다 맞길래 어디서 틀리는 건지 잘 모르겠다.
#정답 아이디어는 뒤에서부터 탐색해서 최대값을 설정하고 이 값보다 작으면 최댓값 - 현재값을 최대 이익에 더해준다.

#느낀점
#그리디 문제는 정방향으로 풀었을 때 잘 안되면 역방향으로 생각해 보는것도 하나의 방법이다.(이 문제도 역방향으로 그리디하게 푸는 문제이다.)

#t = int(input())
#for _ in range(t):
#  n = int(input())
#  price = list(map(int, input().split()))
#  max_list = price[:]
#  max_list.sort(reverse = True)
#  ptr = 0
#  balance = 0 #가진 돈
#  result = 0 #주식
#
#  for i in range(len(price)-1):
#    if price[i] < price[i+1]:
#      balance -= price[i]
#      result += 1
#    else:
#      if max_list[ptr] == price[i]:
#        result *= price[i]
#        balance += result
#        result = 0
#        ptr += 1
#      else:
#        balance -= price[i]
#        result += 1
#    if i == len(price) - 2:
#      if result != 0:
#        balance += result * price[i+1]
#      print(balance)
       
#피드백
t = int(input())
for _ in range(t):
  n = int(input())
  price = list(map(int, input().split()))
  max_price = 0
  result = 0

  for i in reversed(price):
    if max_price < i:
      max_price = i
    elif max_price == i:
      continue
    else:
      result += (max_price - i)
  print(result)
    
  
  