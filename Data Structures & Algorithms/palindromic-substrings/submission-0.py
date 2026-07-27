class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        def expand(l, r):
            nonlocal ans
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ans += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)       # odd-length palindromes
            expand(i, i + 1)   # even-length palindromes

        return ans




