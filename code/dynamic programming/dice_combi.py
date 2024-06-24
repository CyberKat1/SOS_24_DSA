# https://cses.fi/problemset/task/1633

N = int(input())
arr = []
for i in range(N):
    arr.append(-1)
def dicesum(n):
    if n == 1:
        arr[0] = 1
        return 1
    if n <= 0:
        return 0
    if arr[n - 1] != -1:
        return arr[n-1]
    else:
        ans = 1
        for i in range(6):
            ans = ans +dicesum(n - i - 1)
        arr[n - 1] = ans
        return ans
print(dicesum(N))
