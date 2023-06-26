# Move Zeroes
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Constraints:
# a. 1 <= nums.length <= 10^4
# b. -2^31 <= nums[i] <= 2^31 - 1

def moveZeroes(nums):
    zeros = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zeros] = nums[zeros], nums[i]
            zeros += 1
    while zeros < len(nums):
        nums[zeros] = 0
        zeros += 1
      
#example:
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)

                   
