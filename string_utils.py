def reverse_words(text):
    """把句子里的单词顺序倒过来。
    例: 'hello world' -> 'world hello'
    """
    if not isinstance(text, str):
        raise TypeError("reverse_words 需要字符串")
    return " ".join(text.split()[::-1])


def count_vowels(text):
    """数一个字符串里有几个元音字母 (a e i o u，不分大小写)。"""
    if not isinstance(text, str):
        raise TypeError("count_vowels 需要字符串")
    vowels = "aeiou"
    return sum(1 for ch in text.lower() if ch in vowels)


def is_palindrome(text):
    """判断是不是回文 (正着反着一样)，忽略大小写和空格。
    例: 'A man a plan' 不是; 'level' 是。
    """
    if not isinstance(text, str):
        raise TypeError("is_palindrome 需要字符串")
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
