class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        nums3 = nums1 + nums2 
        
        nums3.sort()
        
        if len(nums3) % 2 == 0:
            a = nums3[len(nums3) //2 ]
            b = nums3[len(nums3) // 2 - 1]
            print((a+b) / 2) 
            return (a + b) / 2
        
        else:
            a = len(nums3) // 2
            
            print(a)
            return nums3[a]