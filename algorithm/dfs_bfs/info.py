#DFS / BFS
#자료구조
#스택 (리스트로 구현 가능(append()와 pop() 지원))
#큐 (collections의 deque 사용 (queue = deque(), append(), popleft() 사용))
#유클리드 호제법: 최대공약수 구하는 알고리즘 (두 자연수 a, b,에 대해(a > b) a를 b로 나눈 나머지를 R이라고 하면 a와 b의 최대공약수는 b와 R의 최대공약수와 같다.)
# def gcd(a, b):
#   if a % b == 0:
#     return b
#   else:
#     return gcd(b, a % b)

#DFS(깊이 우선 탐색)
#스택 자료구조(혹은 재귀함수)를 이용
#동작과정
#1. 탐색 시작 노드를 스택에 삽입하고 방문처리
#2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
#3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복한다.
#DFS 예시
# def dfs(graph, v, visited):
#   visited[v] = True
#   print(v, end=' ')
#   for i in graph[v]:
#     if not visited[i]:
#       dfs(graph, i, visited) #재귀
# graph = [
#   [],
#   [2, 3, 8], #1번 노드와 연결된 노드 정보 표현
#   [1, 7], #2번 노드와 연결된 노드 정보 표현
#   [1, 4, 5],
#   [3, 5],
#   [3, 4],
#   [7],
#   [2, 6, 8],
#   [1, 7]
# ]
# visited = [False] * 9
# dfs(graph, 1, visited)

#BFS(너비우선탐색)
#큐 자료구조 이용
#동작과정
#1. 탐색 시작 노드를 큐에 삽입하고 방문처리
#2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
#3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복
#BFS 예시
# from collections import deque

# def bfs(graph, start, visited):
#   queue = deque([start])
#   visited[start] = True
#   while queue:
#     v = queue.popleft()
#     print(v, end = ' ')
#     for i in graph[v]:
#       if not visited[i]:
#         queue.append(i)
#         visited[i] = True

#graph = [
#   [],
#   [2, 3, 8], #1번 노드와 연결된 노드 정보 표현
#   [1, 7], #2번 노드와 연결된 노드 정보 표현
#   [1, 4, 5],
#   [3, 5],
#   [3, 4],
#   [7],
#   [2, 6, 8],
#   [1, 7]
# ]
# visited = [False] * 9
# bfs(graph, 1, visited)


#dfs는 그래프에서 사이클 찾기, 미로탐색, 특정 조건을 만족하는 모든 경우의 수 찾기(백트래킹) 등의 경우에 사용
#bfs는 최단경로, 최소 연결성, 구역 나누기 등의 경우에 사용