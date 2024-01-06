#센서(골드 5)
#내 풀이
#모든 거리를 센 후에 거리 차이가 가장 큰 값이 뭔지 기록
#거리 차이가 나는 두 지점에 기지국 설치
#설치 후 그 거리를 0으로 만들고 반복
#큰 값은 계속해서 갱신
#기지국 개수가 1개남으면 공통적으로 가장 큰 거리차이를 가진 센서들을 방문해서 
#왼쪽부터 본인 센서까지, 본인센서 다음부터 오른쪽 끝까지 더한 값의 차이가 작은 곳에 설치

#진짜 현타 겁나오는 문제
#복잡하게 설계했더니 해결 아이디어는 거리를 내림차순 정렬하고,
#기지국 개수 - 1개 부터 끝까지 더하는거였다..

n = int(input())
k = int(input())
sensor = list(map(int, input().split()))

sensor.sort()
distance = []
for i in range(n - 1):
  distance.append(sensor[i + 1] - sensor[i])
if k >= n:
  print(0)
else:
  distance.sort(reverse=True)
  answer = sum(distance[k-1:])  # 상위 k-1개 거리를 제외한 합
  print(answer)
