
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        another_list = []
        another_list.extend(nums1[0:m])
        another_list.extend(nums2)
        print(nums1, m, nums2, n , another_list)
        global nums1
        nums1 = sorted(another_list)
        # return nums1

obj1 = Solution()
# nums1 = [1,2,3,0,0,0]
print(obj1.merge([1,2,3,0,0,0],  3,  [2,5,6], 3))
# print(nums1)