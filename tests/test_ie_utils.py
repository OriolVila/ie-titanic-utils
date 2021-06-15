import pytest

from ie_utils import tokenize


@pytest.mark.parametrize("sentence, expected_tokens", [
    ("This is a sentence", ["This", "is", "a", "sentence"]),
    ("Another sentence", ["Another", "sentence"])
])
def test_tokenize_returns_expected_list(sentence, expected_tokens):
    #sentence = "This is a sentence"
    #expected_tokens = ["This", "is", "a","sentence"]
    tokens = tokenize(sentence)
    assert tokens == expected_tokens
    
#@pytest.mark.parametrize("sentence, expected_tokens", [
#    ("This is a sentence", ["This", "is", "a", "sentence"]),
#    ("Another sentence", ["Another", "sentence"])    
    
#def test_tokenize_lower_returns_lowercase_tokens(sentence, expected_tokens, lower):
#    if lower == True:
#        tokens = tokenize(lower(sentence))
#        assert tokens == expected_tokens
#    else: 
#        tokens = tokenize(sentence)
#        assert tokens == expected_tokens
    
def test_tokenize_lower_returns_lowercase_tokens():
    sentence = "This is a sentence"
    expected_returns = ["this", "is", "a", "sentence"]
    
    tokens = tokenize(sentence, lower=True)
    
    assert tokens == expected_returns