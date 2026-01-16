nums = [1,1,2,2,3,5,6,7,6,3]


# freq_map = {}

# for i in range(0,len(nums)):
#     if nums[i] in freq_map:
#         freq_map[nums[i]] += 1
#     else:
#         freq_map[nums[i]] = 1

# print(freq_map)


## another method
has_map = {}
n = len(nums)

for i in range(0,n):
    has_map[nums[i]] = has_map.get(nums[i],0)+1

print(has_map)



