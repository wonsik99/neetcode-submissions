class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res= {}

        for i, a in enumerate(nums):
            res[a] = i

        if target in res:
            return res[target]
        else:
            return -1


        