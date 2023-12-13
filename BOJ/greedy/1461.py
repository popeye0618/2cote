#도서관(골드 4)
#내 풀이
#입력 받고, 양수, 음수로 나눈 다음에 정렬(음수는 오름차순, 양수는 내림차순)
#m개씩 묶는다. 묶기 전에 음수, 양수 중 절대값이 가장 큰 값을 결과에서 한 번 뺴준다.(마지막에는 다시 돌아올 필요가 없기 때문에). 묶였던 안묶였던 0번째에 있는 값이 그룹 중에 가장 큰 값이므로, 음수면 절대값을 취해서 2곱하고, 양수면 그냥 2 곱해서 결과에 다 더해준다

def chunk_list(lst, m):
  return [lst[i:i+m] for i in range(0, len(lst), m)]

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

if not len(minus):
  minus.append(0)
if not len(plus):
  plus.append(0)
  

result = 0
if abs(minus[0]) > plus[0]:
  result -= abs(minus[0])
else:
  result -= plus[0]
c_minus = chunk_list(minus, m)
c_plus = chunk_list(plus, m)

for i in range(len(c_minus)):
  result += abs(c_minus[i][0]) * 2
for i in range(len(c_plus)):
  result += c_plus[i][0] * 2

print(result)