class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1 = list(set(nums1))
        nums1.sort()
        
        nums2 = list(set(nums2))
        nums2.sort()
        
        len1 = len(nums1)
        len2 = len(nums2)
        
        ind1 = 0
        ind2 = 0
        
        nums_int = []
        
        while (ind1 < len1) and (ind2 < len2):
            
            if nums1[ind1] < nums2[ind2]:
                ind1 += 1
                
            elif nums1[ind1] > nums2[ind2]:
                ind2 += 1
                
            else:
                nums_int.append(nums1[ind1])
                ind1 += 1
                ind2 += 1
        
        
        return nums_int
