#좌표 압축(실버 2)
#내 풀이
#자기 자신보다 작은 원소의 개수를 찾는다.(중복은 허용 안함)
#bisect를 사용하면 될 것 같다.
#중복을 제거하는 과정에서 리스트 컴프리헨션을 사용하니 시간초과가 났다.
#집합으로 만들고 정렬시키는게 더 효율적이다.

from bisect import bisect_left

n = int(input())
num = list(map(int, input().split()))

tmp = num[:]
ulist = sorted(set(tmp))
answer = []

for x in num:
  answer.append(bisect_left(ulist, x))

print(' '.join(map(str, answer)))