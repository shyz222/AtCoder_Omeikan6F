n = int(input())
m_L = list(map(int,input().split()))

centerl = int(len(m_L)/2-1)
centerr = int(len(m_L)/2)

print(sorted(m_L)[centerr] - sorted(m_L)[centerl])
