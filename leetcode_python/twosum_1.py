class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index , item in enumerate(nums):
            for index1 , item1 in enumerate(nums):
                if index1 > index and item + item1 == target:
                    return [index,index1]

s = Solution()
nums = [2,7,11,15]
target = 9
print(s.twoSum(nums,target))

#复制到系统剪贴板  可视模式下    命令"+y
