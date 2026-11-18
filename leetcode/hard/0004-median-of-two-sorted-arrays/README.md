# Median of Two Sorted Arrays

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return  **the median**  of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

 

Original
Python3
 **Example 1:** 

```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

```

 **Example 2:** 

```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

```

 

 **Constraints:** 

- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -106 <= nums1[i], nums2[i] <= 106

## Solution

**Language:** Python  
**Runtime:** 1 ms (beats 76.33%)  
**Memory:** 19.5 MB (beats 30.97%)  
**Submitted:** 2026-11-18T00:22:31.200Z  

```py
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2
        
        left, right = 0, m
        
        while left <= right:
            i = (left + right) // 2  # Cut in nums1
            j = half - i             # Cut in nums2
            
            # Border elements (handle out-of-bounds with infinity)
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')
            
            # Check if we found the correct partition
            if left1 <= right2 and left2 <= right1:
                if total % 2 == 1:
                    return float(max(left1, left2))
                return (max(left1, left2) + min(right1, right2)) / 2.0
            
            # Adjust binary search boundaries
            elif left1 > right2:
                right = i - 1
            else:
                left = i + 1

```

---

[View on LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays/)