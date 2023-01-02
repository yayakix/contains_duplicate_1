class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        map = {}
        for i in range(len(nums)):
            if map.has_key(nums[i]):
                return True
            else:
