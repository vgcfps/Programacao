nums = [1,6,6,3,8]
target = 12
rashlivre = {}
for i in range(len(nums)):
     diff = target - nums[i]
     if diff in rashlivre:   
       print(rashlivre[diff],i)
     rashlivre[nums[i]] = i
     