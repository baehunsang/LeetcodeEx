import collections
def leastInterval(tasks, n: int) -> int:
        count = collections.Counter(tasks)

        ret = 0
        while True:
            task_count = 0
            for task, _ in count.most_common(n + 1):
                task_count += 1
                ret += 1
                count[task] -= 1
                if count[task] <= 0:
                    del count[task]
            if not count:
                break
            ret += n + 1 - task_count
            
        return ret
def leastInterval2(tasks, n:int)-> int:
	#minimum length of tasks can prove like this
	#(n + 1)*(maximum freqency of task - 1) + (number of maximum freqency tasks)
	#e.g:
	#task = AAAABBBBCD, n = 2
	#AB.AB.AB.AB = ABCABD->idle->AB
	# number of '.' is 3, (4 - 1), so other tasks can insert in '.' part.
	# if '.' is left, it is changed by 'idle'. 
	count = list(collections.Counter(tasks).values())
	max_freq = max(count)
	num_of_max_freq = count.count(max_freq)
	return max(len(tasks), (n + 1)*(max_freq - 1) + num_of_max_freq)
	
print(leastInterval2(['A', 'A', 'A', 'B', 'B', 'B'], 2))