"""
PYTHON SOLUTION - Median of Two Sorted Arrays
08/11/2026
TIME COMPLEXITY: O(log(min(M, N)))
SPACE COMPLEXITY: O(1)
"""
from typing import List

##############
## SOLUTION ##
##############
class Solution:
    
    ##################################
    ## FIND MEDIAN SORTED ARRAYS    ##
    ##################################
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        ####################
        ## EDGE CASE      ##
        ####################
        # Always binary search on the SMALLER array for efficiency
        # (guarantees O(log(min(M,N))) instead of O(log(max(M,N))))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2  # Size of the "left half" after partitioning
        
        ####################
        ## MAIN ALGORITHM ##
        ####################
        # Strategy: Binary Search on Partition Point
        # KEY INSIGHT: The median splits the COMBINED array into a left half
        # and right half of (roughly) equal size. Instead of merging both
        # arrays (O(M+N)), we binary search for the CORRECT partition point
        # in the smaller array - the partition point in the larger array is
        # then determined automatically.
        #
        # A partition is VALID when:
        #   - The left half has exactly total_left elements
        #   - Every element in the left half <= every element in the right half
        #     (checked via: left_max(nums1) <= right_min(nums2) AND
        #                    left_max(nums2) <= right_min(nums1))
        #
        # If left_max(nums1) > right_min(nums2): partition_x is too far RIGHT,
        #   move search range LEFT (decrease partition_x)
        # Otherwise: partition_x is too far LEFT (or already correct),
        #   move search range RIGHT (increase partition_x)
        
        left, right = 0, m
        
        while left <= right:
            partition_x = (left + right) // 2
            partition_y = total_left - partition_x
            
            # Values just around the partition point in nums1
            # Use -infinity/+infinity as sentinels when partition is at an edge
            left_max_x = nums1[partition_x - 1] if partition_x > 0 else float('-inf')
            right_min_x = nums1[partition_x] if partition_x < m else float('inf')
            
            # Values just around the partition point in nums2
            left_max_y = nums2[partition_y - 1] if partition_y > 0 else float('-inf')
            right_min_y = nums2[partition_y] if partition_y < n else float('inf')
            
            # Check if we've found the CORRECT partition
            if left_max_x <= right_min_y and left_max_y <= right_min_x:
                # Valid partition found! Compute the median.
                
                if (m + n) % 2 == 1:
                    # ODD total length: median is the max of the left half
                    return float(max(left_max_x, left_max_y))
                else:
                    # EVEN total length: median is the average of the two
                    # middle values (max of left half, min of right half)
                    return (max(left_max_x, left_max_y) + 
                            min(right_min_x, right_min_y)) / 2.0
            
            elif left_max_x > right_min_y:
                # partition_x is too far right, move search LEFT
                right = partition_x - 1
            else:
                # partition_x is too far left, move search RIGHT
                left = partition_x + 1
        
        # Per problem constraints, valid input always guarantees a solution
        # is found within the loop above.
        raise ValueError("Input arrays are not sorted or otherwise invalid.")

#########
## EOF ##
#########