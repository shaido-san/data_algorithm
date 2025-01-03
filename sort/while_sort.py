my_list = [1, 3, 5, 6, 4, 2]
N = len(my_list)
idx = 0
while idx < N and my_list[idx] <= 4:
    idx += 1
print(idx)