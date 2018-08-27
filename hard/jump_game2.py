class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # print(len(nums))
        maps = {}
        maps[len(nums) - 1] = 0
        self.recursive(nums, maps, len(nums) - 2, 0, len(nums) - 1)
        return maps[0]
        
    def recursive(self, nums, maps, index, minAll, idxMinAll):
        if index < 0:
            return
        if index + nums[index] >= len(nums) - 1:
            maps[index] = 1
            minAll = maps[index]
            idxMinAll = index
            
        elif index + nums[index] >= idxMinAll:
            maps[index] = 1 + minAll
        else:
            temp = float("inf")
            for i in range(1, nums[index] + 1):
                if index + i <= len(nums) - 1:
                    temp = min(temp, maps[index + i])

            maps[index] = 1 + temp
        self.recursive(nums, maps, index - 1, minAll, idxMinAll)