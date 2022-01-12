import collections
def minWindow(s: str, t: str) -> str:
        t_count = collections.Counter(t)
        #num of missing charactor in window
        missing = len(t)
        #exception handling
        l = r = start = end = 0
        for r, char in enumerate(s, 1):
            missing -= t_count[char] > 0
            t_count[char] -= 1
            
            
            if missing == 0:
                while l < r and t_count[s[l]] < 0:
                    t_count[s[l]] += 1
                    l += 1
                if not end or r - l <= end - start:
                    start, end = l, r
                t_count[s[l]] += 1
                l += 1
                missing += 1
	
        return s[start: end + 1]
print(minWindow("a", "aa"))