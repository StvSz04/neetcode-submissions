class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        # If the num of 0's is greater than 1 return all 0's
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1

        if zero_count > 1:
            return [0] * len(nums)

        # If one zero at index i then return 0's but with the product without i

        elif zero_count == 1:
            zero_product = 1

            for num in nums:
                if num != 0:
                    zero_product *= num

            for i in range(len(nums)):
                if nums[i] != 0:
                    res.append(0)
                else:
                    res.append(zero_product)
        else:
            # Otherwise, calculate the total product and divide off the values
            product = 1

            for num in nums:
                product *= num

            print(product)
            for i in range(len(nums)):
                res.append(product // nums[i])

        return res
                    
        