import pytest

from fizzbuzz import fizzbuzz


@pytest.mark.fizz
def test_fizzbuzz_returns_fizz_if_divisible_by_3():
    assert fizzbuzz(3) == "Fizz"


@pytest.mark.buzz
def test_fizzbuzz_returns_buzz_if_divisible_by_5():
    assert fizzbuzz(5) == "Buzz"


@pytest.mark.fizzbuzz
def test_fizzbuzz_returns_fizzbuzz_if_divisible_by_3_and_5():
    assert fizzbuzz(15) == "FizzBuzz"


def test_fizzbuzz_returns_the_number_as_a_string_if_not_divisible_by_3_or_5():
    assert fizzbuzz(4) == "4"
