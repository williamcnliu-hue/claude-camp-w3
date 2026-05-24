import pytest
from string_utils import reverse_words, count_vowels, is_palindrome


# ---------- reverse_words ----------
def test_reverse_words_normal():      # 正常
    assert reverse_words("hello world") == "world hello"

def test_reverse_words_empty():       # 边界：空字符串
    assert reverse_words("") == ""

def test_reverse_words_type_error():  # 异常：传了数字
    with pytest.raises(TypeError):
        reverse_words(123)


# ---------- count_vowels ----------
def test_count_vowels_normal():       # 正常
    assert count_vowels("hello") == 2

def test_count_vowels_none():         # 边界：没有元音
    assert count_vowels("xyz") == 0

def test_count_vowels_type_error():   # 异常
    with pytest.raises(TypeError):
        count_vowels(["a", "b"])


# ---------- is_palindrome ----------
def test_is_palindrome_true():        # 正常：是回文
    assert is_palindrome("level") is True

def test_is_palindrome_false():       # 边界：不是回文
    assert is_palindrome("hello") is False

def test_is_palindrome_type_error():  # 异常
    with pytest.raises(TypeError):
        is_palindrome(3.14)
        