import pytest
from textAnalyzer.textAnalyzer import analyzeText

def test_analyzeText_accepts_text_parameters():
    with pytest.raises(TypeError) as excinfo:
        analyzeText()
    assert "missing 1 required positional argument: 'text'" in str(excinfo.value)

def test_analyzeText_returns_dictionary():
    assert analyzeText("hello 2 times  ") == {
            "textLength":{"withSpaces":15,"withoutSpaces":11},
            "wordCount":3,
            "characterCount":[{"e":2},{"h":1},{"i":1},{"l":2},{"m":1},{"o":1},{"s":1},{"t":1}]
        }
