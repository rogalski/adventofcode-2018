from day04 import solve_1, solve_2, guard_sleep_times


def test_solve_1():
    with open("test_day04.txt") as fh:
        sleep_times_dict = guard_sleep_times(fh)
    assert 240 == solve_1(sleep_times_dict)


def test_solve_2():
    with open("test_day04.txt") as fh:
        sleep_times_dict = guard_sleep_times(fh)
    assert 4455 == solve_2(sleep_times_dict)
