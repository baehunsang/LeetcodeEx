import collections
import functools
import re
import sys
from typing import List
from typing import Optional, Union

#
#class Solution:
#    # Pest your function
#    def is_swap(self, n1, n2):
#        return  str(n1) + str(n2) < str(n2) + str(n1)
#
#    def merge_arr(self, arr1, arr2):
#        if not (arr1 and arr2):
#            return arr1 or arr2
#        l, r = 0, 0
#        ret = []
#        for _ in range(len(arr1)+len(arr2)):
#            if l < len(arr1) and r < len(arr2):
#                if self.is_swap(arr1[l], arr2[r]):
#                    ret.append(arr2[r])
#                    r += 1
#                    continue
#                else:
#                    ret.append(arr1[l])
#                    l += 1
#                    continue
#            if l < len(arr1):
#                ret.append(arr1[l])
#                l += 1
#                continue
#            if r < len(arr2):
#                ret.append(arr2[r])
#                r += 1
#                continue
#        return ret
#                    
#                
#                    
#            
#    def merge_sort(self, nums: List[int]) -> List[int]:
#        if(len(nums) <= 1):
#            return nums
#        mid = len(nums) // 2
#        left = self.merge_sort(nums[:mid])
#        right = self.merge_sort(nums[mid: ])
#        return self.merge_arr(left, right)
#    def largestNumber(self, nums: List[int]) -> str:
#        return str(int(''.join(map(str, self.merge_sort(nums)))))
#
def is_swap(n1:str, n2:str):
        return int(n2 + n1) - int(n1 + n2)
#Using timsort and cmp_to_key function
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        return str(int(''.join(sorted(map(str, nums), key= functools.cmp_to_key(is_swap)))))
    
if __name__ == '__main__':
    
    s = Solution()
    print(s.largestNumber([3, 30, 34, 5, 9]))
