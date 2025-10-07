def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)  # 上
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())  # 右
        if matrix:
            result += matrix.pop()[::-1]  # 下（逆順）
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))  # 左
    return result

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(spiral_order(mat))  # → [1,2,3,6,9,8,7,4,5]