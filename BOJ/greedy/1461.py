#도서관(골드 4)
#내 풀이
#입력 받고, 양수, 음수로 나눈 다음에 정렬(음수는 오름차순, 양수는 내림차순)
#m개씩 묶는다. 묶였던 안묶였던 그룹중에 가장 큰 수를 두 배해서 더하고, 제일 큰 수가 있는 그룹만 제일 큰 수만 더해준다.

n, m = map(int, input().split())
loc = list(map(int, input().split()))
loc.sort()

minus = []
plus = []
for i in loc:
  if i < 0:
    minus.append(i)
  else:
    plus.append(i)
plus.sort(reverse=True)








def chunk_list(lst, m):
  return [lst[i:i+m] for i in range(0, len(lst), m)]

