#암호 해독
#내 풀이
#암호문을 0부터 25까지 모두 더해서 바꿔본다.
#바꾸고나서 사전에 있는 단어가 들어있다면 출력하고 멈춘다.

cipher_text = input()
n = int(input())
words = [input() for _ in range(n)]

for shift in range(26):
  decrypted_text = ""
  for char in cipher_text:
    if 'a' <= char <= 'z':
      decrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    else:
      decrypted_text += char
  if any(word in decrypted_text for word in words):
    print(decrypted_text)
    break