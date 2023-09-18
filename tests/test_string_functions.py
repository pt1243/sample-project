import pytest
from my_package.string_functions import reverse_string, add_exclamation_mark


@pytest.mark.parametrize("test_input,expected", [
    ('abc', 'cba'),
    ('aaa', 'aaa'),
    ('', ''),
])
def test_reverse_string(test_input, expected):
    assert reverse_string(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    ('Hello world', 'Hello world!'),
    ('abc', 'abc!'),
    ('', '!'),
])
def test_add_exclamation_mark(test_input, expected):
    assert add_exclamation_mark(test_input) == expected


def test_reverse_string_raises_typeerror():
    with pytest.raises(TypeError):
        reverse_string(3)


def test_add_exclamation_mark_raises_typeerror():
    with pytest.raises(TypeError):
        add_exclamation_mark(1)
