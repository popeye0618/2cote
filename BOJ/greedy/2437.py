#저울(골드 2)
#내 풀이
#1부터 탐색을 시작해서 우선 같은 무게의 추가 있는지 확인
#없다면 그 값보다 작은 범위에서 조합을 이용해서 목표 무게가 나오는지 확인

#피드백
#조합을 사용하는 경우 지수 시간 복잡도라서 시간초과가 반드시 날 수 밖에 없다.
#누적합을 사용하여 푸는 방식이 좋을 것 같다.

n = int(input())
weight = list(map(int, input().split()))
weight.sort()

ans = 1
for w in weight:
  if w > ans:
    break
  ans += w
  
print(ans)