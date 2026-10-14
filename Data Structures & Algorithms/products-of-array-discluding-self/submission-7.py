class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize my output list
        output = []
        # Iterate through nums and build the final product with 0 handling
        hasZero = False
        total_product = 1

        for num in nums:
            if num != 0 or hasZero:
                total_product *= num
            else:
                hasZero = True

        if nums.count(0) == len(nums):
            total_product = 0

        # Iterate through each index in output and compute the value
        for i in range(len(nums)):
            if hasZero and nums[i] != 0:
                output.append(0)

            elif nums[i] == 0:
                output.append(total_product)
            else:
                output.append(total_product//nums[i])

        # Return output  
        return output 