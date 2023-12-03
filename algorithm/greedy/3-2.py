#큰 수의 법칙
#다양한 수로 이루어진 배열이 있을 때, M번 더하고, 같은 인덱스에 해당하는 수를 연속해서 K번 더할 수 있을 때 큰 수의 법칙 결과를 출력
#입력 조건: 첫째 줄에 N(2 <= N <= 1000), M, K(1 <= M, K <= 10000)의 자연수가 공백을 기준으로 주어진다. 둘째 줄에 N개의 자연수가 주어진다.(10000이하), 입력으로 주어지는 K는 항상 M보다 작거나 같다.

#피드백: 이 방식으로 풀게되면 M의 크기가 매우 커지면 시간초과 판정을 받을 수 있다. 수학적으로 풀어보면 가장 큰 수가 K번 더해지고, 두 번째로 큰 수가 1번 더해지는 수열이 반복되는 것을 알 수 있다. 따라서 이 수열의 길이는 K+1이므로 M을 K+1로 나눈 몫 만큼 반복되고, 나머지는 K보다 작을 것이므로 가장 큰 수를 나머지만큼 더해주면 된다.

#n, m, k = map(int, input().split())
#arr = list(map(int, input().split()))
#
#arr.sort(reverse=True)
#
#cnt = 0
#ans = 0
#for _ in range(m):
#  if cnt == k:
#    ans += arr[1]
#    cnt = 0
#    continue
#  ans += arr[0]
#  cnt += 1
#
#print(ans)

#피드백 코드
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

arr.sort()
first = arr[-1]
second = arr[-2]

t = first * k + second
ans = (t * m // (k + 1)) + (first * (m % (k + 1)))

print(ans)
