#암호 해독
#내 풀이
#단어 탐색하면서 순서가 맞는 경우 그만큼 +해서 원문 구함

n = int(input())
cipher_text = input()
words = [input() for _ in range(n)]

for shift in range(26):
  decrypted_text = ""
  for char in cipher_text:
    if 'a' <= char <= 'z':
      decrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    else:
      decrypted_text += char

  if any(decrypted_text.startswith(word) for word in words):
    print(decrypted_text)
    break
