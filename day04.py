import datetime
import typing
import collections


def guard_sleep_times(seq: typing.Iterable[str]) -> dict:
    seq = sorted(seq)
    guards_per_minute_sleep_time = collections.defaultdict(lambda: [0] * 60)

    active_guard = None
    # is_asleep = False

    prev_event_timestamp = datetime.datetime.fromordinal(1)
    for event in seq:
        this_event_timestamp = datetime.datetime.strptime(event[1:17], "%Y-%m-%d %H:%M")
        if "Guard" in event:
            active_guard = int(event.split()[3][1:])
            # is_asleep = False
        elif "falls" in event:
            pass
            # is_asleep = True
        elif "wakes" in event:
            # is_asleep = False
            delta_minutes = (this_event_timestamp - prev_event_timestamp).seconds / 60
            start_minute = prev_event_timestamp.minute
            for x in range(int(delta_minutes)):
                guards_per_minute_sleep_time[active_guard][(start_minute + x) % 60] += 1
        else:
            raise Exception
        prev_event_timestamp = this_event_timestamp
    return guards_per_minute_sleep_time


def solve_1(guard_sleep_times_dict: dict) -> int:
    guard = max(
        guard_sleep_times_dict.keys(), key=lambda g: sum(guard_sleep_times_dict[g])
    )
    sleep_times = guard_sleep_times_dict[guard]
    return guard * sleep_times.index(max(sleep_times))


def solve_2(guard_sleep_times_dict: dict) -> int:
    guard = max(
        guard_sleep_times_dict.keys(), key=lambda g: max(guard_sleep_times_dict[g])
    )
    sleep_times = guard_sleep_times_dict[guard]
    return guard * sleep_times.index(max(sleep_times))


if __name__ == "__main__":
    with open("day04.txt") as fh:
        guard_sleep_times_data = guard_sleep_times(fh)
    print(solve_1(guard_sleep_times_data))
    print(solve_2(guard_sleep_times_data))
