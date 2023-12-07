#회의실 배정(실버 1)
#내 풀이
#시작 시간순으로 오름차순 정렬을 하고 시작 시간이 같다면 종료시간 기준으로 오름차순 정렬한다. 순서대로 탐색하면서 가장 짧은 종료시간을 갱신, 가장 이른 종료시간보다 작은 시작시간이 없다면 그 종료시간의 회의가 시간표에 들어감. 그 후 그 종료시간을 시작시간으로 가지는 회의의 종료시간을 기준으로 다시 가장 이른 종료시간 갱신. 반복

#피드백
#알고리즘은 맞은것 같은데, 시간초과가 난다.(0 0, 0 0에서 무한반복 발생)
#내 코드는 가장 짧은 종료시간 기준으로 비교 후 그 종료시간보다 더 이른 시작시간이 없을 때, 종료시간을 갱신 후 다시 돌리는데 이 때 result에 1을 더해준다. 따라서 마지막 원소는 검사하지 못한다. 하지만 마지막 원소는 무조건 이전 최소 종료시간보다는 시작시간이 늦을 것이고, 따라서 무조건적으로 포함시킬 수 있다. 반복문 순서 상 마지막 원소의 경우를 result에 더해주지 못하므로 마지막에 1을 더해준다.
#그런데 만약 while문 안의 if문에 한 번도 걸리지 않고 else문에만 걸리는 경우에는 마지막 원소까지 result에 포함시킬 수 있다. 따라서 이 경우 result -1 을 해준다. (flag로 if문에 한 번이라도 걸렸는지 확인)

n = int(input())
arr = []
for _ in range(n):
  row = list(map(int, input().split()))
  arr.append(row)

#첫 번째 원소를 기준으로 정렬, 첫 번째 원소가 같다면 두 번째 원소를 기준으로 정렬
sorted_arr = sorted(arr, key = lambda x:(x[0], x[1]))
result = 0

min_end_time = sorted_arr[0][1]
#처음 성공할 때 안되는 경우를 해결하기 위해 해본 코드
#if sorted_arr[0][0] == sorted_arr[0][1]:
#  result -= 1
flag = False
while len(sorted_arr) > 0:
  if sorted_arr[0][0] < min_end_time:
    flag = True
    if sorted_arr[0][1] < min_end_time:
      min_end_time = sorted_arr[0][1]
    del sorted_arr[0]
  else:
    result += 1
    min_end_time = sorted_arr[0][1]
    del sorted_arr[0]
if flag:
  result += 1
print(result)
    