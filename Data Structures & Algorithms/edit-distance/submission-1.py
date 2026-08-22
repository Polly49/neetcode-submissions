class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def solve(indx1, indx2):
            # CHANGE 1
            if indx1 >= len(word1):
                return len(word2) - indx2

            # CHANGE 2
            if indx2 >= len(word2):
                return len(word1) - indx1

            if (indx1, indx2) in dp:
                return dp[(indx1, indx2)]

            ans = float('inf')

            if word1[indx1] == word2[indx2]:
                ans = min(ans, solve(indx1 + 1, indx2 + 1))

            else:
                # Delete
                ans = min(ans, 1 + solve(indx1+1, indx2))

                # Replace
                ans = min(ans, 1 + solve(indx1 + 1, indx2 + 1))

                # CHANGE 3: Insert
                ans = min(ans, 1 + solve(indx1, indx2 + 1))

            dp[(indx1, indx2)] = ans
            return ans

        return solve(0, 0)