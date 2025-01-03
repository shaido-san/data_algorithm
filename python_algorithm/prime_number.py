# def is_prime(N):
#     if N == 1:
#         return False
    
#     for i in range(2, N):
#         if N % i == 0:
#             return False
    
#     return True

# result = is_prime(257)
# print(result)

# 上のコードは計算量が大きいため書き換える

import math

def is_prime(N):
    if N == 1:
        return False
    
    for i in range(2, int(math.sqrt(N)) + 1):
        if N % i == 0:
            return False
    
    return True

result = is_prime(257)
print(result)