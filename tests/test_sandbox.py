import sandbox


def test_increment():
    assert sandbox.increment() == 1
    assert sandbox.increment(-1) == 0
    assert sandbox.increment(0) == 1
    assert sandbox.increment(1) == 2
    assert sandbox.increment(100) == 101
