class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maps = {len(nums) - 1: True}
        self.iterate(len(nums) - 1, nums, len(nums) - 1, maps)
        return maps[0]
        

    def iterate(self, index, nums, lastGoodIdx, maps):
        if index < 0:
            return
        
        if nums[index] + index >= lastGoodIdx:
            maps[index] = True
            lastGoodIdx = index
        else:
            maps[index] = False
        
        self.iterate(index - 1, nums, lastGoodIdx, maps)