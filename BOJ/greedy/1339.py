#단어 수학(골드 4)
#다시 풀어봐야할 문제
#내 풀이
#수의 최대 길이는 8이므로 크기가 8인 2차원 리스트를 만들어서 각 자릿수에 들어오는 알파벳을 행으로 한다. 그 리스트를 뒤집어서 큰 자릿수부터 빈도가 가장 많은 알파벳에 9부터 지정해준다.
#빈도 분석 아이디어가 생각이 나지 않아서, 차선책으로 자릿수마다 점수를 매기는데, 최대 8자리이므로, 1의 자리는 1점, 10의 자리는 10점 이런 순으로 가서 점수가 젤 높은 알파벳부터 높은 배점 차지

#피드백
#딕셔너리는 생각했는데, 처음써봐서 어떻게 쓰는지 배우는 문제가 됐다.
#아이디어는 1. 알파벳을 딕셔너리에 저장(단어의 길이에 따라 알파벳의 자릿수가 정해지므로, 자릿수를 체크하여 그 자리에 맞는 값을 매칭시킨다.)
#(1의 자리면 1, 10의 자리면 10, 100의 자리면 100) 이 아이디어는 아까 내가 낸 아이디어랑 비슷한 것 같다.
#2. 매칭을 완료한 후에 딕셔너리의 value값을 가져와서 리스트에 내림차순 정렬한다.
#3. 이 리스트에 9부터 차례로 곱하면 최대값을 얻을 수 있다.

n = int(input())
word = []
word_dict = {}
score = []
for _ in range(n):
  word.append(input())

for i in range(n):
  for j in range(len(word[i])):
    if word[i][j] in word_dict:
      word_dict[word[i][j]] += 10 ** (len(word[i]) - j - 1)
    else:
      word_dict[word[i][j]] = 10 ** (len(word[i]) - j - 1)
      
for val in word_dict.values():
  score.append(val)
score.sort(reverse = True)

sum = 0
pow = 9

for i in score:
  sum += pow * i
  pow -= 1

print(sum)
