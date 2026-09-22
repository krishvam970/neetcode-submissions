class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        columns=len(matrix[0])
        total=rows*columns
        l=0
        r=total-1
        while l<=r:
            mid = (l+r)//2
            row= mid//columns
            column = mid%columns
            if matrix[row][column]==target:
                return True 
            elif matrix[row][column]<target:
                l = mid+1
            else :
                r = mid -1 
        return False
        