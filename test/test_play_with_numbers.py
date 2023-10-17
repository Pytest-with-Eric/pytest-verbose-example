from src.play_with_numbers import smallest_number, highest_number, number_to_string

# Tests the smallest_number() function
def test_smallest_number():
    assert smallest_number([10, 5, 9]) == 5

# Tests the highest_number() function
def test_highest_number():
    assert highest_number([10, 5, 9]) == 10

# Tests the number_to_string() function
def test_number_to_text():
    assert number_to_string(7) == number_to_string(5)