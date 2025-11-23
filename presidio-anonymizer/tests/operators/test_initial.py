import pytest
from presidio_anonymizer.operators import Initial

def test_correct_name():
    assert Initial().operator_name() == "initial"

def test_initials_basic():
    assert Initial().operate("John Smith") == "J. S."
    assert Initial().operate("john smith") == "J. S."

def test_initials_extra_whitespace():
    text = "     Eastern    Michigan   University "
    assert Initial().operate(text) == "E. M. U."

def test_initials_special_char():
    text = " @abc "
    assert Initial().operate(text) == "@A."
    
def test_initials_with_leading_symbols():
    assert Initial().operate("@abc") == "@A."
    assert Initial().operate("@843A") == "@8."
    assert Initial().operate("--**abc") == "--**A."

