T=int(input())

def floor(n):
    return((n+9)//10)

for _ in range(T):
    x,y=map(int, input().split())
    print(abs(floor(x)-floor(y)))
