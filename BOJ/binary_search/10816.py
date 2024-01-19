#숫자 카드 2(실버 4)
#내 풀이
#bisect 이용해서 풀면 된다.

from bisect import bisect_left, bisect_right

def cal(v):
  left = bisect_left(cards, v)
  right = bisect_right(cards, v)
  return right - left

n = int(input())
cards = list(map(int, input().split()))
cards.sort()
m = int(input())
needs = list(map(int, input().split()))

answer = []
for v in needs:
  answer.append(cal(v))

print(' '.join(map(str, answer)))