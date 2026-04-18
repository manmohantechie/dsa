from typing import List


class TwoSum:
    """
    LeetCode - https://leetcode.com/problems/two-sum/description/
    ---------------------
    Given an array of integers `nums` and an integer `target`,
    return indices of the two numbers that add up to target.

    Constraints:
        - Exactly one solution exists
        - Cannot use the same element twice
        - Return answer in any order
    """

    def brute(self, nums: List[int], target: int) -> List[int]:
        """
        Brute Force — Check every pair of elements.

        Algorithm:
            For each element nums[i], scan every element nums[j]
            after it to see if nums[i] + nums[j] == target.

        Time  : O(n²) — nested loops over all pairs
        Space : O(1)  — no extra data structures
        """
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):       # j > i to avoid reusing same index
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []   # unreachable given problem constraints

    def optimal(self, nums: List[int], target: int) -> List[int]:
        """
        Hash Map — Single pass with O(1) complement lookup.

        Algorithm:
            For each num, compute complement = target - num.
            If complement was seen before, we found our pair.
            Otherwise, store num and its index for future lookups.

        Time  : O(n) — one pass; hash map insert/lookup is O(1) avg
        Space : O(n) — hash map stores up to n elements
        """
        seen = {}   # num -> index

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:          # O(1) average lookup
                return [seen[complement], i]

            seen[num] = i                   # record for future iterations

        return []   # unreachable given problem constraints
