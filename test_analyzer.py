from file_analyzer import count_words, count_chars, find_most_common_word

def test_count_words():
    assert count_words("Hello world") == 2
    # Test empty string
    assert count_words("") == 0
    # Test with multiple single-character words
    assert count_words("A B C") == 3
    # Test with punctuation
    assert count_words("Hello, world!") == 2
    # Test with single word
    assert count_words("Hello") == 1
    # Test with unique words
    assert count_words("Write clean, modular, and testable Python code.") == 7
    # Test with multiple spaces
    assert count_words("   Leading and trailing spaces   ") == 4


def test_count_chars():
    assert count_chars("Hello world") == 11
    # Test empty string
    assert count_chars("") == 0
    # Test with multiple single-character words
    assert count_chars("A B C") == 5
    # Test with punctuation
    assert count_chars("Hello, world!") == 13
    # Test with single word
    assert count_chars("Hello") == 5
    # Test with unique words
    assert count_chars("Write clean, modular, and testable Python code.") == 47
    # Test with multiple spaces
    assert count_chars("   Leading and trailing spaces   ") == 33


def test_most_common_word():
    assert find_most_common_word("Hello world") == "Hello"
    # Test empty string
    assert find_most_common_word("") == "(Empty String)"
    # Test with multiple single-character words
    assert find_most_common_word("A B C A B C") == "A"
    # Test with punctuation
    assert find_most_common_word("Hello, world!") == "Hello,"
    # Test with single word
    assert find_most_common_word("Hello") == "Hello"
    # Test with unique words
    assert find_most_common_word("Write clean, modular, and testable Python code.") == "Write"
    # Test with multiple spaces
    assert find_most_common_word("   Leading and trailing spaces   ") == "Leading"