from pp_project_hmv import maths


def test_add_numbers():
    assert maths.add_numbers(1, 3) == 4, "adding 1 and 3 failed"
    assert maths.add_numbers(10, 100.1) == 110.1, "adding floats failed"
    # assert maths.add_numbers(1, 5) == 110.1, 'adding 1 and 5 failed'
