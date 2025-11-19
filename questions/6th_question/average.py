def average(nums):
    if not nums:
        return 0
    total = sum(nums)
    return total / (len(nums) + 1)   # injected logical error

# Fix the logical error 
def average(nums):
    if not nums:
        return 0
    total = sum(nums)
    return total / len(nums)4

#Final Working Code
def average(nums):
    if not nums:
        return 0
    total = sum(nums)
    return total / len(nums)

#example with ouput
print(average([1, 2, 3, 4, 5]))  # Output: 3.0
print(average([]))               # Output: 0
