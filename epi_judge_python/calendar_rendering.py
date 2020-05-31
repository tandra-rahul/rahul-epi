import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))

def find_max_simultaneous_events(A: List[Event]) -> int:
    # TODO - you fill in here.
    #Building list of endpoints
    E = [p for event in A for p in (Endpoint(event.start, True),
                                    Endpoint(event.finish, False))]

    #Sort endpoints
    E.sort(key=lambda e: (e.time, not e.is_start))

    num_conc, max_conc = 0, 0
    for endpoint in E:

        if endpoint.is_start:
            num_conc += 1
            max_conc = max(max_conc, num_conc)
        else:
            num_conc -= 1

    return max_conc


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
