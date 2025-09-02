import random

class ZobristHashing:
    def __init__(self, rows=8, cols=8, pieces="Pp"):
        self.rows = rows
        self.cols = cols
        self.pieces = pieces
        self.table = {
            (r, c, p): random.getrandbits(64)
            for r in range(rows) for c in range(cols) for p in pieces
        }
        self.hash_value = 0

    def compute_hash(self, board):
        h = 0
        for r in range(self.rows):
            for c in range(self.cols):
                piece = board[r][c]
                if piece != ".":
                    h ^= self.table[(r, c, piece)]
        self.hash_value = h
        return h

    def update(self, r, c, old_piece, new_piece):
        if old_piece != ".":
            self.hash_value ^= self.table[(r, c, old_piece)]
        if new_piece != ".":
            self.hash_value ^= self.table[(r, c, new_piece)]
        return self.hash_value


if __name__ == "__main__":
    board = [
        list("........"),
        list("........"),
        list("........"),
        list("........"),
        list("....P..."),
        list("........"),
        list("........"),
        list("........"),
    ]
    zob = ZobristHashing()
    h1 = zob.compute_hash(board)
    print("初期ハッシュ:", h1)
    zob.update(4, 4, "P", ".")
    zob.update(3, 4, ".", "P")
    print("移動後ハッシュ:", zob.hash_value)