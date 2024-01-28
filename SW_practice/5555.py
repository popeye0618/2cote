#반지 (실버 5)
#내 풀이
#문자열 검색
#맨 뒤와 맨 앞이 연결되어 있다고 했으니 찾을 문자열의 길이만큼 더 붙여주자

find = input()
n = int(input())
length = len(find)
result = 0
for _ in range(n):
  rings = input()
  rings = rings[:] + rings[:length]
  if find in rings:
    result += 1

print(result)