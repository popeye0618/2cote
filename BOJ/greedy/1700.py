#멀티탭 스케쥴링(골드 1)
#내 풀이
#처음에 꽂는 멀티탭은 어떤 기준으로 정할까
#우선 맨 처음으로 오는 콘센트는 반드시 꽂아야함
#그 다음부턴 빈도순으로 꽂는게 좋아보이긴 함
#딕셔너리 사용해서 빈도 세놓고 꽂을 때마다 1씩 빼는 방법 괜찮을듯

#피드백
#문제의 핵심 아이디어는 두 가지였다.
#우선 그리디적으로 내가 사용한 방식은 맞았지만 중요한 아이디어는
#해당 전기용품이 다음에 등장하는 것이 언제인지 기록하고
#현재 꽂혀있는 전기용품 중에서 가장 나중에 다시 꽂힐 전기용품을 빼준다.

n, k = map(int, input().split())
arr = list(map(int, input().split()))
now = []
answer = 0

for i in range(k):
  if arr[i] in now:
    continue
    
  if len(now) < n:
    now.append(arr[i])
    continue

  #현재 꽂혀있는 전기용품 중에서 다음에 언제 등장하는지 기록
  #등장하지 않는다면 K로 설정해서 제일 나중에 등장한다고 생각함
  next_use = [k] * len(now)
  for j in range(len(now)):
    for t in range(i + 1, k):
      if now[j] == arr[t]:
        next_use[j] = t
        break
  #현재 꽂혀있는 전기용품 중 등장을 제일 늦게하는 전기용품을 뽑고
  #현재 탐색중인 전기용품을 꽂는다.
  idx = next_use.index(max(next_use))
  now.pop(idx)
  now.append(arr[i])
  answer += 1

print(answer)