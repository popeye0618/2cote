#빙고

def check(result):
  for i in range(5):
    if all(my[j][i] == 0 for j in range(5)):
      result += 1
      if result >= 3:
        return result
    if all(my[i][j] == 0 for j in range(5)):
      result += 1
      if result >= 3:
        return result

  if all(my[i][i] == 0 for i in range(5)):
    result += 1
    if result >= 3:
      return result
  if all(my[i][4 - i] == 0 for i in range(5)):
    result += 1
    if result >= 3:
      return result

  return result


my = []
orders = []
for _ in range(5):
  my.append(list(map(int, input().split())))
for _ in range(5):
  orders.append(list(map(int, input().split())))

cnt = 0
result = 0
for i in range(5):
  for order in orders[i]:
    cnt += 1
    for j in range(5):
      for k in range(5):
        if my[j][k] == order:
          my[j][k] = 0
          if cnt >= 5:
            result = check(0)
            if result >= 3:
              print(cnt)
              exit(0)
