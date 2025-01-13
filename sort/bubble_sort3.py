def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]

data = [6, 3, 5, 9, 2, 4, 1, 8, 10, 7]
bubble_sort(data)
print(data)