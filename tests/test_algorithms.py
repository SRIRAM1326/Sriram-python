import pytest
from tests.conftest import load_project_module

def test_calculator_operations():
    calc = load_project_module("01_calculator_cli")
    assert calc.add(10, 5) == 15
    assert calc.subtract(10, 4) == 6
    assert calc.multiply(3, 7) == 21
    assert calc.divide(20, 4) == 5.0
    assert "Error" in calc.divide(10, 0)

def test_palindrome_checker():
    pal = load_project_module("12_palindrome_checker")
    assert pal.is_palindrome("racecar") is True
    assert pal.is_palindrome("A man, a plan, a canal: Panama") is True
    assert pal.is_palindrome("Was it a car or a cat I saw?") is True
    assert pal.is_palindrome("Python") is False

def test_prime_number_checker():
    prime = load_project_module("13_prime_number_checker")
    assert prime.is_prime(2) is True
    assert prime.is_prime(3) is True
    assert prime.is_prime(17) is True
    assert prime.is_prime(97) is True
    assert prime.is_prime(0) is False
    assert prime.is_prime(1) is False
    assert prime.is_prime(4) is False
    assert prime.is_prime(100) is False

def test_anagram_checker():
    ana = load_project_module("17_anagram_checker")
    assert ana.is_anagram("listen", "silent") is True
    assert ana.is_anagram("The Eyes", "They See") is True
    assert ana.is_anagram("hello", "world") is False

def test_leap_year_checker():
    leap = load_project_module("18_leap_year_checker")
    assert leap.is_leap_year(2024) is True
    assert leap.is_leap_year(2000) is True
    assert leap.is_leap_year(1900) is False
    assert leap.is_leap_year(2023) is False
