#모험가 길드
#한 마을에 모험가가 N명 있다. 모험가 길드에서 N명의 모험가를 대상으로 '공포도'를 측정했고, 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 한다.
#N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 문제

#내 풀이
#공포도가 낮은 순서대로 정렬 후 총 모험가 수에서 빼면서 최대 그룹의 수를 구한다.

#피드백
#내 방식은 단순히 공포도가 작은 사람을 기준으로 그룹을 만들었는데, 이 경우 공포도가 더 큰 사람은 이 그룹에 들어가기 위해 더 많은 사람이 필요하므로 단순히 빼는 연산으로는 답을 구할 수 없다.

#n = int(input())
#data = list(map(int, input().split()))
#result = 0

#data.sort()

#for i in data:
#  if n - i > 0:
#    n -= i
#    result += 1

#print(result)

#피드백 코드
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  # 총 그룹의 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in data:  # 공포도를 낮은 것부터 하나씩 확인하며
  count += 1  # 현재 그룹에 해당 모험가를 포함시키기
  if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
    result += 1
    count = 0

print(result)
