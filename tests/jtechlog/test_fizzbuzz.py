from jtechlog.fizzbuzz import fizzbuzz


def test_for_many():
    assert fizzbuzz(16) == "1 2 fizz 4 buzz fizz 7 8 fizz buzz 11 fizz 13 14 fizzbuzz 16"
