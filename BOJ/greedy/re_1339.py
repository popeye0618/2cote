#단어 수학(골드 4)
#내 풀이
#단어를 입력받고, 딕셔너리에 알파벳을 저장
#우선순위인 자릿수와 빈도를 판단하기 위해 각 자리수마다 점수를 부여
#마지막으로 딕셔너리를 value 내림차순으로 정렬하고 리스트로 만들어서
#다시 딕셔너리에 앞에서부터 순차적으로 9부터 부여
#돌면서 자릿수만큼 10을 제곱해주고 ans에 더해준다.

n = int(input())
words = []
my_dict = {}

for _ in range(n):
  words.append(input())

for word in words:
  for j in range(len(word)):
    score = 10 ** (len(word) - j)
    if word[j] not in my_dict:
      my_dict[word[j]] = score
    else:
      my_dict[word[j]] += score

result = [key for key , value in sorted(my_dict.items(), key = lambda x : x[1], reverse = True)]

t = 9
for alp in result:
  my_dict[alp] = t
  t -= 1

answer = 0
for word in words:
  for j in range(len(word)):
    answer += my_dict[word[j]] * (10 ** (len(word) - (j + 1)))
print(answer)