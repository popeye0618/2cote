#방 번호(실버 5)
#내 풀이
#문자열로 받고, 0부터 9가 몇 개 나오는지 카운트 하면서, 6이나 9가 나오면 6과 9 중 카운트가 작은 쪽으로 넣는다. 같으면 자기 숫자에 넣고 마지막에 젤 큰 값 출력

#피드백
#처음엔 리스트를 내림차순 정렬해서 처음 원소를 출력했지만, max()함수를 사용하는 것이 더 효율적이다.
s = input()
cnt = [0 for _ in range(10)]

for i in s:
  if i == '6' or i == '9':
    if cnt[6] > cnt[9]:
      cnt[9] += 1
    elif cnt[6] < cnt[9]:
      cnt[6] += 1
    else:
      cnt[int(i)] += 1
  else:
    cnt[int(i)] += 1
    
print(max(cnt))
  
