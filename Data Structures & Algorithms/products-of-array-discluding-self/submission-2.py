class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []

        product = 1
        for num in nums:
            prefix.append(product)
            product *= num

        product = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix.append(product)
            product *= nums[i]

        postfix.reverse()

        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])

        return res