def answer(n):
    pri = [True for i in xrange(n + 1)]
    p = 2
    while p * p <= n:
        if pri[p]:
            for i in xrange(p * 2, n + 1, p):
                pri[i] = False
        p += 1
    return pri
 
pri = answer(8000)
arr = []
n = int(raw_input())
for i in xrange(2, n + 1):
    if pri[i]:
        arr.append(i)
        final = set()
for i in xrange(len(arr)):
    for j in xrange(len(arr)):
        final.add(int(str(arr[i]) + str(arr[j])))
count = 0
final = list(final)
for i in xrange(len(final)):
    if pri[final[i]]:
        count=count+1
print count
