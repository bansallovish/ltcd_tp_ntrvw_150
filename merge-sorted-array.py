class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for j in range(n):
            nums1[m+j] = nums2[j]
        nums1.sort()

obj1 = Solution()
# nums1 = [1,2,3,0,0,0]
print(obj1.merge([1,2,3,0,0,0],  3,  [2,5,6], 3))
# print(nums1)