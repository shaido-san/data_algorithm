def mandelbrot(width=80, height=40, max_iter=30):
    for y in range(height):
        line = ""
        for x in range(width):
            # 複素平面上の座標にマッピング
            re = (x - width / 2) * 4.0 / width
            im = (y - height / 2) * 2.0 / height
            c = complex(re, im)
            z = 0
            i = 0
            while abs(z) <= 2 and i < max_iter:
                z = z * z + c
                i += 1
            # 表示：濃さで区別
            chars = " .:-=+*#%@"
            line += chars[min(i * len(chars) // max_iter, len(chars) - 1)]
        print(line)

mandelbrot()