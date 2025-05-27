import math

# クエリとその答えを入れる
class Query:
    def __init__(self, l, r, idx):
        self.l = l
        self.r = r
        self.idx = idx

def mo_algorithm(arr, queries):
    block_size = int(math.sqrt(len(arr)))
    queries.sort(key=lambda q: (q.l // block_size, q.r))

    answers = [0] * len(queries)
    freq = {}
    distinct = 0
    l, r = 0, -1

    for q in queries:
        while r < q.r:
            r += 1
            freq[arr[r]] = freq.get(arr[r], 0) + 1
            if freq[arr[r]] == 1:
                distinct += 1
        while r > q.r:
            freq[arr[r]] -= 1
            if freq[arr[r]] == 0:
                distinct -= 1
            r -= 1
        while l < q.l:
            freq[arr[l]] -= 1
            if freq[arr[l]] == 0:
                distinct -= 1
            l += 1
        while l > q.l:
            l -= 1
            freq[arr[l]] = freq.get(arr[l], 0) + 1
            if freq[arr[l]] == 1:
                distinct += 1

        answers[q.idx] = distinct

    return answers

arr = [1, 1, 2, 1, 3]
queries = [Query(0, 4, 0), Query(1, 3, 1), Query(2, 4, 2)]

results = mo_algorithm(arr, queries)
print(results)  