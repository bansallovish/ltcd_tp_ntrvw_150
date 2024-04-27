class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_arr = [nums[0]]
        temp = nums[0]
        for i in nums[1:]:
            if i == temp:
                continue
            else:
                temp = i
                new_arr.append(i)

        for i in range(0,len(new_arr)):
            nums[i] = new_arr[i]

        # print(nums)
        return len(new_arr)


obj1=Solution()
print("2",obj1.removeDuplicates([1,1,2]))
print("5",obj1.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
# print("",obj1.removeDuplicates())
# print("",obj1.removeDuplicates())
# print("",obj1.removeDuplicates())
