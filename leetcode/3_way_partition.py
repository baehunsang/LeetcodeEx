import collections
import functools
import re
import sys
from typing import List
from typing import Optional, Union


class Solution:
    # Pest your function
    def sortColors(self, nums: List[int]) -> None:
        less, runner, high = 0 ,0 ,len(nums)
        while runner < high:
            if nums[runner] == 1:
                runner += 1
            elif nums[runner] > 1:
                high -= 1
                nums[runner], nums[high] = nums[high], nums[runner]
            else:
                nums[runner], nums[less] = nums[less], nums[runner]
                less += 1
                runner += 1




if __name__ == '__main__':
    
    s = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    print(s.sortColors(nums))
    print(nums)
