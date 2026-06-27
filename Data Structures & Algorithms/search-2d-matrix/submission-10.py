class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start=0
        end=len(matrix)-1
        while(start<end):
            mid=int((start+end+1)/2)
            if (matrix[mid][0]<=target):
                start=mid
            else:
                end=mid-1

        k=start
        start=0
        end=len(matrix[0])-1
        if matrix[k][0]>target:
            return False
        while(start<=end):
            mid=int((start+end)/2)
            if matrix[k][mid]==target:
                return True
            elif matrix[k][mid]>target:
                end=mid-1
            else:
                start=mid+1
        return False
