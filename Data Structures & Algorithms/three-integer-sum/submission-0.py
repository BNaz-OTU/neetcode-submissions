class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        final = []
        nums.sort()

        for idx in range(len(nums)):
            if (idx > 0 and nums[idx] == nums[idx - 1]):
                continue

            val = nums[idx]

            left = idx + 1
            right = len(nums) - 1

            while left < right:
                l_val = nums[left]
                r_val = nums[right]

                threeSum = val + l_val + r_val

                if (threeSum == 0):
                    final.append([val, l_val, r_val])

                    while left < right and l_val == nums[left]:
                        left += 1

                
                elif (threeSum > 0):
                    right -= 1
                
                else:
                    left += 1
            
        return final
