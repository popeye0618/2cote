#부분 문자열

while True:
  try:
    s, t = input().split()
    si, ti = 0, 0

    while si < len(s) and ti < len(t):
      if s[si] == t[ti]:
        si += 1
      ti += 1

    if si == len(s):
      print('Yes')
    else:
      print('No')
  except EOFError:
    break