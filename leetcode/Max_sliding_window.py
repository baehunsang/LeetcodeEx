import sys
import collections
def max_sliding_window(nums, k):
	prev_max = -sys.maxsize
	ret = []
	window = collections.deque()
	
	for i, num in enumerate(nums):
		window.append(num)
		if i < k - 1:
			continue
		#first condition
		if prev_max == -sys.maxsize:
			prev_max = max(window)
		#condotion to change max num
		elif prev_max < num:
			prev_max = num
		ret.append(prev_max)
		#slide window and reset prev_max
		#If the input arr sorted by decrising order, the time complexity become O(k*n)(worst case)
		if prev_max == window.popleft():
			prev_max = -sys.maxsize
	return ret
	
def max_sliding_window_2(nums, k):
        ret = []
        window = collections.deque()
        for i  in range(len(nums)+1):
            if i >= k:
                ret.append(nums[window[0]])
                if window[0] < i - k + 1:
                    window.popleft()
              #In this code snippet, the worst time complexity when pushing the value to the stack is O(n), but the time complexity by the amortization analysis is O(1){O(n)/n}. Therefore, this code can be solved in time complexity O(n) while ensuring that window[0] is the maximum of the corresponding window.
            while i < len(nums) and window and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)
        return ret
	
print(max_sliding_window_2([1, 3, -1, -3, 5, 3, 6 ,7], 3))