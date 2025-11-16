from app import greet


def test_greet():
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"


def test_farewell():
    assert farewell("Alice") == "Goodbye, Alice!"
