class KMPMatcher:
    def __init__(self, pattern):
        self.pattern = pattern
        self.lps = self._compute_lps_array()

    def _compute_lps_array(self):
        lps = [0] * len(self.pattern)
        length = 0  # length of the previous longest prefix suffix
        i = 1

        while i < len(self.pattern):
            if self.pattern[i] == self.pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def search(self, text):
        m = len(self.pattern)
        n = len(text)
        i = j = 0  # i: index for text, j: index for pattern
        results = []

        while i < n:
            if self.pattern[j] == text[i]:
                i += 1
                j += 1

            if j == m:
                results.append(i - j)
                j = self.lps[j - 1]
            elif i < n and self.pattern[j] != text[i]:
                if j != 0:
                    j = self.lps[j - 1]
                else:
                    i += 1
        return results


# 使い方
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
matcher = KMPMatcher(pattern)
matches = matcher.search(text)

print("パターンが見つかった位置:", matches)