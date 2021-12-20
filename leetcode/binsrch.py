import collections
import functools
import re
import sys
from typing import List
from typing import Optional, Union


class Solution:
    # Pest your function
    def search(self, nums: List[int], target: int) -> int:
        def binSrch(l, r, nums, target):
            if l <= r:
                mid = l + (r - l)//2
                if nums[mid] > target:
                    return binSrch(l, mid - 1, nums, target)
                if nums[mid] < target:
                    return binSrch(mid + 1, r, nums, target)
                if nums[mid] == target:
                    return nums[mid]
            else:
                return -1
        return binSrch(0, len(nums) - 1, nums, target)




if __name__ == '__main__':
    
    s = Solution()
    print(s.search([-1, 0, 3, 5, 9, 12], 9))
