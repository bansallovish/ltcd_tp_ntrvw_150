class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counter = 0
        n = len(nums)
        for i in range(n-1 , -1 , -1):
            if nums[i] == val:
                nums.pop(i)
                nums.append(val)
                counter+=1

        
        # print(nums)
        return n-counter

obj1 = Solution()
print(obj1.removeElement([3,2,2,3],3))
print(obj1.removeElement([0,1,2,2,3,0,4,2],2))