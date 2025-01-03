# my_list = [1, 3, 2, 5, 4, 9]

# max_valu = my_list[0]
# for val in my_list[1:]:
#     if max_valu < val:
#         max_valu = val

# print("最大値：", max_valu)

# # ユークリッドの互除法 どこで終わるのかが繰り返し処理中に判明するような処理はwhileを使うのがいい

# def my_gcd(a, b):
#     if b == 0:
#         return a
    
#     m = a % b
#     return my_gcd(b, m)

# x = my_gcd(144, 84)
# print(x)

# def gcd(c, d):
#     while d != 0:
#         gcd = d
#         d = c % d
#         c = gcd
    
#     return gcd

# y = gcd(144, 84)
# print(y)

#復習

text = "xの値:{x}, yの値:{y}"
x = 100
y = 200
print(text.format(x=x, y=y))
