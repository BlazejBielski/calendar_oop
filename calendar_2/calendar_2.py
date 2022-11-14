import datetime
from pprint import pprint

from event import Event, Workshop, Reminder
from helpers import generate_objects


class Calendar:
    def __init__(self, events=None):
        self._events = events or []

    @property
    def events(self):
        counter = 0

        for event in self._events:
            if datetime.datetime.now() < event.start_date <= datetime.datetime.now() + datetime.timedelta(weeks=4):
                counter += 1

        return f'For incoming four weeks, you have {counter} events'

    @events.setter
    def events(self, value):

        if not isinstance(value, (Event, Workshop, Reminder)):
            raise TypeError('Wrong data type.')

        self._events.append(value)

    def filter_by_date(self, start_date=datetime.datetime.min, end_date=datetime.datetime.max):

        events = []

        for event in self._events:
            if start_date <= event.start_date < end_date:
                events.append(event)

        return events

    def __len__(self):
        return len(self._events)


data = generate_objects()
calendar = Calendar(data)
filter_a = calendar.filter_by_date()
filter_r = calendar.filter_by_date(datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(weeks=4))
print(len(filter_r))
print(len(filter_a))
pprint(calendar.events)

