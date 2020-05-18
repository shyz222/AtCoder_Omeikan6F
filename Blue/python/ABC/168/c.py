import math
A, B, H, M = map(int, input().split())
H_rad = ((H*30) + 0.5*M) % 360
M_rad = M*6 % 360
kari_kakudo = max(H_rad,M_rad) - min(H_rad,M_rad)
kakudo = math.radians(min(kari_kakudo,360-kari_kakudo))
ans = (pow(A,2)+pow(B,2))-2 * A * B * (math.cos(kakudo))
print(math.sqrt(ans))