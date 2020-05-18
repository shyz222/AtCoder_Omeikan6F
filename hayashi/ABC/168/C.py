import sys
import math
input = sys.stdin.readline

A, B, H, M = map(int, input().rstrip().split())


H_theta = 30 *( H + M * (1/60))
M_theta = M * 6
theta = min(abs(H_theta - M_theta), 360 - abs(H_theta - M_theta))
ans = math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(math.radians(theta)))
print(ans)
