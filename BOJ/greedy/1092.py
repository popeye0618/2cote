#배(골드 5)
#내 풀이
#여러 풀이를 생각했는데, 진짜 하나하나 비교해서 옮기는 것이라고는 생각을 못했다.

#피드백
#결국 정답을 보고야 말았다. 막상 보니 좀 더 고민해볼걸 이라는 생각이 들고, 그리디는 브루트포스로도 가는구나 라는 생각도 들었다.
#문제해결 방법은 큰 박스부터 지우기 위해 둘 다 내림차순 정렬을 하고, 박스는 지우는 족족 리스트에서 제거한다. 박스리스트의 크기가 0이 될 때까지 돌리며, n번 돌릴 때 마다 결과에 1을 더해주면 된다.
#이렇게 브루트포스 형식이 들어갈 것 같으면 최대한 적게 수행하기 위해 앞에서 조건들로 자르고 들어가는 것이 좋다.

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))
result = 0

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if boxes[0] > cranes[0]: #다 옮길 수 없는경우
  result = -1
elif cranes[-1] >= boxes[0]: #모든 크레인을 사용해서 끝까지 다 옮길 수 있는 경우
  result = m // n
  if m % n != 0:
    result += 1
else: #어떤 크레인 용량보다 무거운 박스가 있는 경우
  while len(boxes) > 0:
    for crane in cranes:
      for box in boxes:
        if crane >= box:
          boxes.remove(box)
          break
    result += 1
    
print(result)