class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
     l,r=0,len(numbers)-1
     while l<r:
        t=numbers[l]+numbers[r]
        if t== target:
            return [l+1,r+1]
            
        elif t>target:
            r=r-1
        elif t<target:
            l=l+1
     else:
        return -1
        
        
        