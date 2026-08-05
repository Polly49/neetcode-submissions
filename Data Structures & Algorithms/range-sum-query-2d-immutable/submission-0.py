class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.nums=matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1=row1
        c1=col1
        r2=row2
        c2=col2
        sm=0
        for i in range (r1,r2+1):
            for j in range(c1,c2+1):
                sm+=self.nums[i][j]
        return sm


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)