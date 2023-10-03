import pytest

CONFIG = {"bool_value": True, "string": "abc", "integer": 123}


def bool_value():
    return CONFIG["bool_value"]

#########################################################################


def test_bool_value_true():
    """Test that "bool_value" is True"""
    assert bool_value() is True


def test_bool_value_false(monkeypatch):
    """Test that "bool_value" is False"""

    monkeypatch.setitem(CONFIG, "bool_value", False)

    assert bool_value() is False


def test_key_error(monkeypatch):
    """Test that KeyError raises if "bool_value" is deleted"""

    monkeypatch.delitem(CONFIG, "bool_value", raising=False)

    with pytest.raises(KeyError):
        bool_value()


def test_bool_value_true_again():
    """Test that "bool_value" is True"""
    assert bool_value() is True
