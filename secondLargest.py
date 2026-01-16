user_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

print (type(numbers))
def find_second_largest(nums):
    if len(nums) < 2:
        return -1
    largest = secondLargest = float('-inf')
    for num in nums:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num != largest and num > secondLargest:
            secondLargest = num
    
    if secondLargest == float('-inf'):
        return -1
    
    return secondLargest

result = find_second_largest(numbers)
print("The second largest number is:", result)