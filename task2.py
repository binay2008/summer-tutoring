# ==============================================================================
# GROUP B: SEARCH & DEDUPLICATION ALGORITHMS (BRANCH: feature/search-algorithms)
# ==============================================================================

# --- TASK B1: Deduplicate While Preserving Order ---
def remove_duplicates_keep_order(items: list) -> list:
    """
    Remove duplicates from a list while PRESERVING the original order of items.
    (Standard set(items) loses order!).

    Example:
    [4, 2, 4, 1, 2, 3] -> [4, 2, 1, 3]

    Hint: Use an empty list for output and a set 'seen' to track visited elements in O(1).
    """
    # TODO: Iterate through items, use 'seen' set to check if item was already added
    seen_numbers = set()
    results = []
    for item in items:
        if item not in seen_numbers:
            results.append(item)
            seen_numbers.add(item)
    return results


# --- TASK B2: Find First Duplicate Element ---
def find_first_duplicate(nums: list[int]) -> int:
    """
    Find and return the FIRST element that appears more than once.
    If there are no duplicates, return -1.

    Example:
    [2, 5, 1, 2, 3, 5] -> 2 (since 2 appears second time first)
    [1, 2, 3, 4] -> -1
    """
    # TODO: Use a set to track numbers you have seen so far
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1

# --- TASK B3: Binary Search for Target Insertion ---
def binary_search_first_greater(arr: list[int], target: int) -> int:
    """
    Given a SORTED list of numbers, use Binary Search to find
    the index of the FIRST element that is strictly GREATER than 'target'.
    If no such element exists, return -1.

    Example:
    arr = [10, 20, 30, 40, 50], target = 25
    Result -> Index 2 (value 30)
    """
    # TODO: Implement Binary Search to locate element > target
    low = 0
    high = len(arr) - 1
    index = 0
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            low = mid + 1
            index = mid
        else: 
            high = mid - 1
    return index + 1

# --- TEST PRINTS FOR STUDENT ---
if __name__ == "__main__":
    print("--- Task B1: Keep Order Deduplication ---")
    raw_list = ["apple", "banana", "apple", "cherry", "banana"]
    print("Deduplicated:", remove_duplicates_keep_order(raw_list))

    print("\n--- Task B2: First Duplicate ---")
    print("First duplicate in [3, 1, 4, 1, 5, 3]:", find_first_duplicate([3, 1, 4, 1, 5, 3]))
    print("First duplicate in [1, 2, 3]:", find_first_duplicate([1, 2, 3]))

    print("\n--- Task B3: Binary Search First Greater ---")
    numbers = [10, 20, 30, 40, 50]
    print("First > 25 index in [10, 20, 30, 40, 50]:", binary_search_first_greater(numbers, 25))