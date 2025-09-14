t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    door = list(map(int, input().split()))
    closed = [i + 1 for i in range(n) if door[i] == 1]
    if not closed:
        print("YES")
    else:
        span = closed[-1] - closed[0] + 1
        print("YES" if span <= x else "NO")
