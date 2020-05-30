import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
sticks = list(map(int, input().rstrip().split()))

sorted_sticks = sorted(sticks, reverse=True)
print(sum(sorted_sticks[:K]))
