def radix_sort(arr):
    #Sort a list of non-negative integers using LSD Radix Sort.
    if len(arr) == 0:
        return []
    
    # Find maximum number to know number of digits
    max_num = max(arr)
    exp = 1  # Start with units digit
    
    # Copy the list so we don't change original
    result = arr[:]
    
    while max_num // exp > 0:
        # Create 10 buckets (0-9)
        buckets = [[] for _ in range(10)]
        
        # Put numbers into buckets based on current digit
        for num in result:
            digit = (num // exp) % 10
            buckets[digit].append(num)
        
        # Flatten buckets back into result
        idx = 0
        for bucket in buckets:
            for num in bucket:
                result[idx] = num
                idx += 1
        
        exp *= 10  # Move to next digit
    
    return result


# DEMO 
if __name__ == "__main__":
    print("\nRadix Sort Demo:")
    nums = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Original:", nums)
    sorted_nums = radix_sort(nums)
    print("Sorted:  ", sorted_nums)