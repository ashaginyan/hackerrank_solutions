from solution import print_function
import sys


def test_printfunction(capsys):
    print_function(5)
    captured = capsys.readouterr()
    assert captured.out == "12345\n"

    print_function(3)
    captured = capsys.readouterr()
    assert captured.out == "123\n"

def test_printfunction_min_constraint(capsys):
    print_function(1)
    captured = capsys.readouterr()
    assert captured.out == "1\n"
