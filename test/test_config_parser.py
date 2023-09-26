import pytest
from src.config_parser import parse_config

def test_empty_config():
    result = parse_config("")
    assert result == {}

def test_single_config():
    result = parse_config("username=alice")
    assert result == {"username": "alice"}

def test_multiple_configs():
    result = parse_config("username=alice; age=30; country=US")
    assert result == {
        "username": "alice",
        "age": "30",
        "country": "US"
    }

def test_configs_with_spaces():
    result = parse_config(" username = alice ; age = 30 ; country = US ")
    assert result == {
        "username": "alice",
        "age=": "30",
        "country": "US"
    }
