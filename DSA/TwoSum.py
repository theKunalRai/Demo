class Solution(object):
    def twoSum(self, nums, target):
#        """
#        :type nums: List[int]
#        :type target: int
#        :rtype: List[int]
#        """
#        for i in range(len(nums)):
#            for j in range(1,len(nums)):
#                if nums[i]+nums[j] == target:
#                    return [i,j]

# Optimal Solution
numMap = {} # Creating an empty dictionary 

for i, num in enumerate(nums):
    
    complement = target - num # Calculate the complement
    if complement in numMap: # Check if the complement exists in numMap
        return [numMap[complement], i] 
    
    numMap[num] = i # Add the num in numMap if the complement is not in numMap

return []
