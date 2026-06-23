class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mx = 0
        for char in set(s):
            i = 0
            j = 0
            current_k = k
            while j < len(s):
                if s[j] == char:
                    mx = max(mx, j - i + 1)
                    j += 1
                elif s[j] != char and current_k > 0:
                    current_k -= 1
                    mx = max(mx, j - i + 1)
                    j += 1
                else:
                    if s[i] != char:
                        current_k += 1
                    i += 1
        return mx