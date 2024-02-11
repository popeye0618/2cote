#암호 해독

n = input()
k = input()

length = len(k) // len(n)
arr = []

temp = list(n)
temp.sort()

for i in range(len(n)):
  arr.append([temp[i], i, k[length * i : length * i + length]])

arr.sort(key = lambda x : x[1])
ans = []

while arr:
  for i in n:
    for j in range(len(arr)):
      if arr[j][0] == i:
        ans.append(arr[j])
        arr.pop(j)
        break

result = ''
for i in range(length):
  for j in range(len(n)):
    result += ans[j][2][i]

print(result)
