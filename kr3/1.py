lst = [1,2,'a',3,4,'b','c','d','e']

print((lambda strs, nums: {s: nums[i] if i < len(nums) else 0 for i, s in enumerate(strs)})(strs=[s for s in lst if isinstance(s, str)], nums=[n for n in lst if isinstance(n, int)][::-1]))
