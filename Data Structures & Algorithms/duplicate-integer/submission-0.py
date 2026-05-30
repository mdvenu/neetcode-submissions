class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ans = set(nums)
        return not len(ans)==len(nums)

        