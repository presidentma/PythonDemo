import sys
sys.setrecursionlimit(10000)
def iterator1(n):
    if n <= 1:
        return 1
    else:
        return n * iterator1(n - 1)

print(iterator1(3000))
