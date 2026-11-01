class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        numsHolder = [0] * 100001
        count = 0
        final = []

        for idx in range(k):
            val = nums[idx]
            if numsHolder[val] == 0:
                count += 1
            
            numsHolder[val] += 1
        
        final.append(count)
        left = 0

        for right in range(k, len(nums)):
            rightVal = nums[right]
            leftVal = nums[left]

            if numsHolder[rightVal] == 0:
                count += 1

            numsHolder[rightVal] += 1
            
            
            if numsHolder[leftVal] == 1:
                count -= 1

            numsHolder[leftVal] -= 1
            
            left += 1
            final.append(count)
        
        return final

        

