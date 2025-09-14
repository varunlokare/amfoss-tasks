T=int(input())
for _ in range(T):
    N,X,Y=map(int, input().split())
    capacity=(N+1)*Y
    if capacity >=X:
        print("YES")
    else:
        print("NO")
