print("Hello World!")
# ==============================================================================
# GROUP A: SETS & COMBINED ALGORITHMS (BRANCH: feature/set-algorithms)
# ==============================================================================

# --- TASK A1: Find Common Followers (Sets) ---
def find_common_followers(user1_followers: list[str], user2_followers: list[str]) -> set:
    """
    Given two lists of follower usernames, return a SET of usernames
    that follow BOTH users (intersection).

    Example:
    user1 = ["alice", "bob", "charlie"]
    user2 = ["bob", "david", "charlie"]
    Result -> {"bob", "charlie"}
    """
    # TODO: Convert lists to sets and use intersection (&)
    followers_user1 = set(user1_followers)
    followers_user2 = set(user2_followers)
    return followers_user1 & followers_user2






# --- TASK A2: Unique Characters Check ---
def has_all_unique_chars(text: str) -> bool:
    """
    Check if a given string contains all UNIQUE characters (case-insensitive, ignore spaces).
    Return True if all characters are unique, otherwise False.

    Example:
    "Python" -> True
    "Java" -> False (letter 'a' repeats)

    Hint: Compare the length of the string with the length of its set.
    """
    # TODO: Clean string (lowercase, remove spaces) and check length vs set length
    new_text = text.strip().lower().replace(' ', '')
    return len(new_text) == len(set(new_text))


# --- TASK A3: Find Missing Number (Sets + Search) ---
def find_missing_number(nums: list[int], n: int) -> int:
    """
    You are given a list 'nums' containing unique numbers from 1 to 'n',
    but ONE number is missing. Find and return that missing number.

    Example:
    nums = [1, 2, 4, 5], n = 5
    Result -> 3

    Hint: Create a full set from range(1, n + 1) and find the difference with set(nums).
    """
    # TODO: Use set difference (-) to find the missing element
    new_nums = set(range(1, n + 1))
    answer = new_nums - set(nums)
    return answer


# --- TEST PRINTS FOR STUDENT ---
if __name__ == "__main__":
    print("--- Task A1: Common Followers ---")
    u1 = ["alex", "john", "maria", "steve"]
    u2 = ["maria", "kate", "alex", "andrew"]
    print("Result:", find_common_followers(u1, u2))

    print("\n--- Task A2: Unique Chars ---")
    print("'Lamp' is unique?:", has_all_unique_chars("Lamp"))
    print("'Banana' is unique?:", has_all_unique_chars("Banana"))

    print("\n--- Task A3: Missing Number ---")
    print("Missing in [1, 3, 4, 5] (n=5):", find_missing_number([1, 3, 4, 5], 5))
