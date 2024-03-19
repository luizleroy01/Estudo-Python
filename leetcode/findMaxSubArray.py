# This function iterates through the array, updating the count of 0s and 1s encountered so far. 
#It uses a hashmap to store the running count as keys and their corresponding indices as values.
# If the same count is encountered again, it calculates the length of the subarray and updates the maximum length if necessary.
# Finally, it returns the maximum length found.

def findMaxLength(nums):
    max_length = 0
    count = 0
    hash_map = {0: -1}

    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1

        if count in hash_map:
            max_length = max(max_length, i - hash_map[count])
        else:
            hash_map[count] = i

    return max_length

# Test cases
nums1 = [0, 1]
nums2 = [0, 1, 0]

print(findMaxLength(nums1))  # Output: 2
print(findMaxLength(nums2))  # Output: 2
