#문자열 재정렬
#알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다.
#모든 알파벳을 오름차순으로 정렬하여 출력 후, 모든 숫자를 더한 값을 이어서 출력

s = input()
alp = []
sum = 0
for i in s:
  if i.isdigit():
    sum += int(i)
  else:
    alp.append(i)
alp.sort()

if sum != 0:
  alp.append(str(sum))

#join()함수는 문자열 리스트를 하나의 문자열로 결합해 줌
print(''.join(alp))
