x = int(input())
for _ in range(x):
    y = int(input())
    buckets = list(map(int, input().split()))
    sums = sum(buckets)
    if sums**.5 == int(sums**.5):
        print('Yes')
    else:
        print('NO')   