import math

def count_primitive_triangles(N):
    count = 0
    for x1 in range(-N, N + 1):
        for y1 in range(-N, N + 1):
            if (x1, y1) == (0, 0): continue
            if math.gcd(x1, y1) != 1: continue
            for x2 in range(-N, N + 1):
                for y2 in range(-N, N + 1):
                    if (x2, y2) == (0, 0) or (x2 == x1 and y2 == y1): continue
                    if math.gcd(x2, y2) != 1: continue
                    area = abs(x1 * y2 - x2 * y1)
                    if area == 0:
                        continue  # 共線
                    if area % 2 == 1:
                        count += 1
    return count // 6  # 三角形の順列の重複を除く

print("格子点ゼロ三角形の数:", count_primitive_triangles(10))