#잃어버린 괄호(실버 2)
#내 풀이
#-를 만나면 다음 -가 나올 때 까지 괄호를 친다. 그 후 eval() 내장함수를 이용해 수식을 계산한다.
#홀수번 째 -에는 뒤에 '('를, 짝수번 째 -에는 앞에 ')'를 삽입한다.(문자열 슬라이싱 이용)
# -가 홀수 개인경우 끝나지 않으므로 이 경우 마지막에 ')'를 삽입한다.
#'00009'같은 경우를 처리해야한다. 따라서 eval()함수를 사용하지 못하고, 반복문으로 계산해야할 것 같다.
s = input()
length = len(s)
chk = 1
ptr = 0
for i in range(len(s)):

  if s[ptr] == '-':
    if chk % 2 != 0:
      s = s[:ptr+1] + '(' + s[ptr+1 :]
      ptr += 1
      i += 1
      chk = 0
    else:
      s = s[:ptr] + ')' + s[ptr :]
      chk = 1
  ptr += 1

if chk == 0:
  s = s[:len(s)] + ')'

#맨 처음이나 부호 뒤가 0인경우 0000x의 경우이기에 이 경우 + 0 뒤에 붙여준다.
t = False
if s[0] == '0':
  t = True  
new_s = ""

for i in range(len(s)):
    if not t:
        if s[i] in {'-', '+', '(', ')'} and i < len(s) - 1 and s[i + 1] == '0':
            t = True
    else:
        if s[i] in {'-', '+', '(', ')'}:
            new_s += '+0'
            t = False

    if i < len(s):
        new_s += s[i]

print(eval(new_s))