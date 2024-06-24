# https://atcoder.jp/contests/dp/tasks/dp_a

N = int(input())
arr = [int(x) for x in input().split()]
scores = []
for t in range(N):
    scores.append(-1)
def frog(i):
    if scores[i - 1] != -1:
        return scores[i-1]
    if i == N:
        scores[i -1] = 0
        return 0
    if i == N - 1:
        scores[i - 1] = abs(arr[N - 1] - arr[N-2])
        return scores[i - 1]
    #if scores[i - 1] != 0:
     #   return scores[i-1]
    else:
        scores[i - 1] = min(frog(i+1) + abs(arr[i] - arr[i - 1]) , frog(i + 2) + abs(arr[i + 1] - arr[i - 1]))
        return scores[i - 1]
print(frog(1)) 
                            