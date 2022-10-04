#given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A. codity question

A=(12,2,3,4,54,6,2,1331,0)
x=12

def sol(i,A):
    n = sorted(i for i in set(A) if i > 0)  # Remove duplicates and negative numbers
    if not n:
        return 1
    kucuk=min(n)
    buyuk=max(n)
    for x in range(kucuk,buyuk):
        if x not in n:
            return x
        return 1

print(sol(x,A))
