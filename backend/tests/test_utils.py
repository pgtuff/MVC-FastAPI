import pytest
from app.utils import miles_to_kms  # Import the function to test

# Test cases for miles_to_kms function
test_cases = [
    (0, 0),  # 0 miles should be 0 kilometers
    (1, 1.60934),  # 1 mile should be 1.60934 kilometers
    (5, 8.0467),  # 5 miles should be 8.0467 kilometers
    (10, 16.0934),  # 10 miles should be 16.0934 kilometers
    (100, 160.934),  # 100 miles should be 160.934 kilometers
]

@pytest.mark.parametrize("miles, expected_kms", test_cases)
def test_miles_to_kms(miles, expected_kms):
    # Assert that the result is approximately equal to the expected value
    result = miles_to_kms(miles)
    assert round(result, 5) == round(expected_kms, 5), f"Failed for {miles} miles"
