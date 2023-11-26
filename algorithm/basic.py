n = int(input())
data = list(map(int, input().split()))
a, b, c = map(int, input().split())

print(n)
print(data)
print(a, b, c)

#빠르게 입력받기
import sys

data = sys.stdin.readline().rstrip()
print(data)

#f-string (python 3.6부터 사용가능)
answer = 7
print(f"정답은 {answer}입니다.")

#람다 표현식 (1. 어떠한 함수 자체를 입력으로 받는 또 다른 함수를 사용할 때 사용
#혹은 2. 여러개의 리스트에 하나의 규칙을 적용할 때)
print((lambda a, b: a + b)(3, 7))

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]


def my_key(x):
  return x[1]


print(sorted(array, key=my_key))
#1번의 경우
print(sorted(array, key=lambda x: x[1]))

#2번의 경우
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
result = map(lambda a, b: a + b, list1, list2)
print(list(result))

#유용한 표준 라이브러리
#1. itertools (순열, 조합 등)
#2. heapq (heap자료구조 제공(우선순위 큐 구현 위해 사용))
#3. bisect (이진 탐색 기능 제공)
#4. collections (deque, Counter 등 유용한 자료구조 포함)
#5. math (필수적인 수학적 기능 제공 (팩토리얼, 제곱근, 최대공약수, 삼각함수, 파이 등))

#내장함수
#sum(), min(), max(), eval(): 문자열로 된 수식을 수 형태로 반환
#sorted(): 리스트 정렬, 키 속성으로 정렬 기준 지정 가능, reverse=True: 역순 정

#1. itertools
#순열: 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는 것
#조합: 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3))  #모든 순열 구하기
print(result)

from itertools import combinations

result = list(combinations(data, 2))  #모든 조합 구하기
print(result)

from itertools import product

result = list(product(data, repeat=2))  #2개를 뽑는 모든 순열 구하기(중복 허용)
print(result)

from itertools import combinations_with_replacement

result = list(combinations_with_replacement(data,
                                            2))  #2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)

#4. collections
#Counter
from collections import Counter

counter = Counter(['red', 'blue', 'blue', 'green', 'red', 'red', 'red'])

print(counter['blue'])  #'blue'가 등장한 횟수 출력
print(counter['green'])  #'green'이 등장한 횟수 출력
print(dict(counter))  #사전 자료형으로 반환

#5. math
import math


#최소 공배수(LCM)를 구하는 함수
def lcm(a, b):
  return a * b // math.gcd(a, b)


a = 21
b = 14
print(math.gcd(21, 14))  #최대 공약수(GCD) 계산
print(lcm(21, 14))  #최소 공배수(LCM) 계산
