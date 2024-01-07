#공항(골드 2)
#내 풀이
#고려해야 할 점이 몇 가지 보인다.
#우선 비행기가 도킹 가능한 게이트 중 가장 큰 번호로 가는 것이 좋아보인다.
#왜냐면 나중에 들어오는 비행기가 더 작은 게이트 번호를 가질 수 있기 때문
#게이트가 차 있으면 1 줄이면서 비어있으면 들여보낸다.

#피드백
#내 코드도 분명히 잘 동작하는 코드이다.
#하지만 최대 입력 범위가 10^5이며, 제한 시간은 1초이므로
#이중 for문이 아닌 새로운 알고리즘을 사용해야했다.
#바로 union-find 알고리즘이다.

# g = int(input())
# p = int(input())
# plane = [0]
# for _ in range(p):
#   plane.append(int(input()))

# gate = [False] * (g + 1)

# answer = 0
# for i in range(1, len(plane)):
#   if gate[plane[i]] == False:
#     gate[plane[i]] = True
#     answer += 1
#   else:
#     chk = False
#     for j in range(plane[i], 0, -1):
#       if gate[j] == False:
#         gate[j] = True
#         answer += 1
#         chk = True
#         break
#     if not chk:
#       break

# print(answer)

#피드백 (유니온-파인드 알고리즘 사용)
#경로 압축까지 사용


def find_parent(gate, x):
  if gate[x] != x:
    gate[x] = find_parent(gate, gate[x])
  return gate[x]


g = int(input())
p = int(input())
#부모 테이블을 자기 자신으로 초기화
gate = [i for i in range(g + 1)]
answer = 0

for _ in range(p):
  plane = int(input())
  docking_gate = find_parent(gate, plane)
  #밑에있는 주석을 참고했을 때, x = 1이며 gate[x] = 1인 경우까지 사용했다면,
  #그 다음상황은 gate[x] = 0이 될 것이며 0은 존재하지 않으므로 더이상 도킹할 수 없다는 뜻
  #따라서 반복문을 탈출한다.
  if docking_gate == 0:
    break
  #union 부분
  #gate[docking_gate]를 이미 사용했으니 -1번째 게이트로 연결시킨다.
  #따라서 find_parent()로 넘어갔을 때 x는 3인데 gate[x]는 2이므로
  #재귀적으로 돌아가서 x = 2와 gate[x] = 2이므로 비어있다고 판단해서
  #2로 넣고, gate[docking_gate] = 1 이 될 것이다.
  gate[docking_gate] = gate[docking_gate - 1]
  answer += 1
print(answer)
