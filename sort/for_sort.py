my_list = [1, 3, 5, 6, 4, 2]
N = len(my_list)
idx = None
for i in range(N):
    if 4 < my_list[i]:
        idx = i
        break
print(idx)