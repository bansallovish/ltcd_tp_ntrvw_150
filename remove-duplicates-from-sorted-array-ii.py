class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        temp = nums[0]
        new_arr = [nums[0]]
        for i in range(1,len(nums)):
            # print(nums[i])
            if nums[i] == temp:
                c+=1
            else:
                temp = nums[i]
                c=0

            if c==0 or c==1:
                new_arr.append(nums[i])

        for i in range(0,len(new_arr)):
            nums[i] = new_arr[i]

        # print(nums)
        return len(new_arr)

obj1=Solution()
print("5",obj1.removeDuplicates([1,1,1,2,2,3]))
print("7",obj1.removeDuplicates([0,0,1,1,1,1,2,3,3]))
# print("",obj1.removeDuplicates())
# print("",obj1.removeDuplicates())
# print("",obj1.removeDuplicates())

'''
        for i in range(1,len(nums)-1-k):
            if nums[i] == temp:
                c+=1
            else:
                temp = nums[i]
                c=0

            if c>1:
                c+=1
                k+=1
                nums.append(nums[i])
                nums.pop(i)
'''