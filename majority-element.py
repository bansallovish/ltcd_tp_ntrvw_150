class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= len(nums)
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
            if dict[i] > n/2:
                return i
    

obj1= Solution()
print("3",obj1.majorityElement([3,2,3]))
print("2",obj1.majorityElement([2,2,1,1,1,2,2]))
# print("",obj1.majorityElement())
# print("",obj1.majorityElement())
# print("",obj1.majorityElement())
# print("",obj1.majorityElement())
