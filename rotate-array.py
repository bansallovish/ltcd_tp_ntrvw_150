class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        nums = self.reverse_list(nums,0,n-1)
        print(nums)
        nums[0:k] = self.reverse_list(nums[0:k],0,k-1)
        print(nums)
        nums[k:n] = self.reverse_list(nums[k:n],0,n-k-1)
        print(nums)

        return nums
    
    def reverse_list(self,arr,left,right):
        print(left,right)
        while (left < right):
            # Swap
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right -= 1
    
        return arr


obj1=Solution()
print("[5,6,7,1,2,3,4]",obj1.rotate([1,2,3,4,5,6,7],3))
print("[3,99,-1,-100]",obj1.rotate([-1,-100,3,99],2))
# print("",obj1.rotate())
# print("",obj1.rotate())
# print("",obj1.rotate())
# print("",obj1.rotate())