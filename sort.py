
class sort:
    def count_sort(nums, max_value):
        output = [0 for i in range(max_value+1)]
        count = [0 for i in range(max_value+1)]

        for i in nums:
            count[i] += 1

        for i in range(max_value+1):
            count[i] += count[i-1]

        for i in range(len(nums)-1, -1, -1):
            output[count[nums[i]]-1] = nums[i]
            count[nums[i]] -= 1

        return output

x = [3, 6, 4, 1, 3, 4, 1, 4]
print(sort.count_sort(x, max(x)+1))
