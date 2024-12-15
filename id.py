# x = [1, 2, 3,]
# y = x
# print(id(x))
# print(id(y))

# x = [4, 5]
# print(id(x))

# 再代入すると、メモリの位置が変わる。

def myfunc(x):
    print(id(x))

x = [1, 2, 3]
print(id(x))
myfunc(x)

#変数やメソッドを定義すると、呼び出した際に因数で変数がコピーされて新たにメモリが消費されるわけではない。

#空間計算量の改善例,下のコードはnumbersで新たにメモリを確保することになるが、足し上げた後はそのリストが不要になる。

# def my_func():
#     numbers = []
#     for i in range(100):
#         if i % 3 == 0:
#             numbers.append(i)
    
#     return numbers

# def main():
#     numbers = my_func()
#     my_sum = 0
#     for num in numbers:
#         my_sum += num
    
#     print(my_sum)

# main()

#改善
def main():
    my_sum = 0
    for i in range(100):
        if i % 3 == 0:
            my_sum += i
    
    print(my_sum)

main()