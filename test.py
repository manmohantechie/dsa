import pytest
from script import TwoSum


@pytest.fixture
def solver():
    return TwoSum()


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------

def check(result: list, nums: list, target: int):
    """Assert the returned indices are valid for the given input."""
    assert len(result) == 2, "Must return exactly 2 indices"
    i, j = result
    assert i != j,               "Indices must be distinct"
    assert nums[i] + nums[j] == target, "Values at indices must sum to target"


# ------------------------------------------------------------------
# Shared test cases (parametrized)
# ------------------------------------------------------------------

CASES = [
    # (nums,                target, description)
    ([2, 7, 11, 15],        9,      "basic example from problem statement"),
    ([3, 2, 4],             6,      "answer is not index 0"),
    ([3, 3],                6,      "duplicate values"),
    ([1, 2, 3, 4, 5],       9,      "answer at end of array"),
    ([-1, -2, -3, -4, -5], -8,      "all negative numbers"),
    ([0, 4, 3, 0],          0,      "zeros that sum to target"),
    ([1000000, 2, 999998],  1000000, "large values"),
]


@pytest.mark.parametrize("nums, target, description", CASES)
def test_brute(solver, nums, target, description):
    result = solver.brute(nums[:], target)   # pass a copy to avoid mutation side-effects
    check(result, nums, target)


@pytest.mark.parametrize("nums, target, description", CASES)
def test_optimal(solver, nums, target, description):
    result = solver.optimal(nums[:], target)
    check(result, nums, target)


# ------------------------------------------------------------------
# Consistency: both methods must agree on every case
# ------------------------------------------------------------------

@pytest.mark.parametrize("nums, target, description", CASES)
def test_brute_and_optimal_agree(solver, nums, target, description):
    brute   = solver.brute(nums[:], target)
    optimal = solver.optimal(nums[:], target)
    # Both must be valid (indices may differ in order for some problems,
    # so we compare as sets of index pairs rather than raw lists)
    assert sorted(brute) == sorted(optimal), (
        f"Methods disagree for nums={nums}, target={target}: "
        f"brute={brute}, optimal={optimal}"
    )


# ------------------------------------------------------------------
# Edge cases
# ------------------------------------------------------------------

def test_minimum_input(solver):
    """Array of length 2 — only one possible pair."""
    nums, target = [1, 9], 10
    for method in (solver.brute, solver.optimal):
        result = method(nums[:], target)
        check(result, nums, target)


def test_negative_and_positive_mix(solver):
    nums, target = [-3, 4, 3, 90], 0
    for method in (solver.brute, solver.optimal):
        result = method(nums[:], target)
        check(result, nums, target)


def test_returns_list(solver):
    """Return type must be a list."""
    nums, target = [2, 7], 9
    assert isinstance(solver.brute(nums, target),   list)
    assert isinstance(solver.optimal(nums, target), list)
