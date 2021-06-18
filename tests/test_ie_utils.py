import pytest
import pandas as pd
from numpy.testing import assert_array_almost_equal

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
    
    
def test_series_are_approximately_equal():
    ser = pd.Series([0.1,0.2, 0.1+0.2])
    expected_ser= pd.Series([0.1,0.2, 0.3])
    
    assert_array_almost_equal(ser, expected_ser)
    assert 0.1 + 0.2 == pytest.approx(0.3)
    
    
def test_tokenize_remove_stopwords():
    sentence = "I have a dog"
    expected_tokens = ["I", "have", "dog"]
    
    tokens = tokenize(sentence, remove_stopwords=True)
    assert tokens == expected_tokens
    
def test_tokenize_remove_punctuaction():
    sentence = "I found your .dog!!"
    expected_tokens = ["I", "found", "your", "dog"]
    
    tokens = tokenize(sentence, remove_punctuation=True)
    assert tokens == expected_tokens
    


    