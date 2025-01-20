def liner_search(mylist, val):
    for i, n in enumerate(mylist):
        if n == val:
            print(str(i) + "番目に見つかりました")
            return
        
    print("見つかりませんでした")

l = [1, 5, 3, 7, 2, 4, 8, 9]
liner_search(l, 7)