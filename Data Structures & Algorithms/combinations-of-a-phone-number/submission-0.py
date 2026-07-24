class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        a={
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        res=[]
        def backtracking(i,currStr):
            if len(currStr)==len(digits):
                res.append(currStr)
                return
            for ch in a[digits[i]]:
                backtracking(i+1,currStr+ch)
        backtracking(0,"")
        if not digits:
            return []
        return res                 


