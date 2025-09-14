t=int(input().strip())
for _ in range(t):
    n=int(input())
    arr=list(map(int, input().split()))
    freq = [0]*11
    for num in arr:
        if 1<=num<=10:
            freq[num] += 1
    min_moves = n 
    for i in range(1, 11):
        moves = n-freq[i]
        if moves < min_moves:
            min_moves = moves 
    print(min_moves)
