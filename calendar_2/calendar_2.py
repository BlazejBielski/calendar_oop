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

    def filter_by_duration(self, duration=None, duration_min=0, duration_max=None):

        if duration is not None:
            duration_min = duration_max = duration

        events = []

        for event in self._events:
            if event.duration in range(duration_min,
                                       (duration_max + 1 if duration_max is not None else event.duration + 1)):

                events.append(event)

        return events

    def _filter_by_duration(self, **kwargs):
        events = []

        for event in self._events:
            attr = getattr(event, 'duration', None)
            if attr and attr in range(kwargs.get('min', 0), kwargs.get('max', attr + 1)):
                events.append(event)

        return events

    def _filer_by_title(self, **kwargs):
        events = []

        for event in self._events:
            attr = getattr(event, 'title', None)
            if attr and kwargs.get('search_text', '') in attr:
                events.append(event)

        return events

    def _filter_by_description(self, **kwargs):
        events = []

        for event in self._events:
            attr = getattr(event, 'description', None)

            if attr and kwargs.get('search_text', '') in attr:
                events.append(event)

        return events

    def _filter_by_owner(self, **kwargs):
        events = []

        for event in self._events:
            attr = getattr(event, 'owner', None)

            if attr and kwargs.get('search_name', '') in attr:
                events.append(event)

        return events

    def _filer_by_participants(self, **kwargs):
        events = []

        for event in self._events:
            attr = getattr(event, 'participants', None)

            if attr and kwargs.get('search_name', '') in attr:
                events.append(event)

        return events
    def filter(self, filter_name, **kwargs):

        options = {
            'duration': self._filter_by_duration,
            'title': self._filer_by_title,
            'description': self._filter_by_description,
            'owner': self._filter_by_owner,
            'participants': self._filer_by_participants,
        }

        return options.get(filter_name)(**kwargs)

    def __len__(self):
        return len(self._events)


data = generate_objects()
calendar = Calendar(data)
filter_a = calendar.filter_by_date()
filter_duration = calendar.filter_by_duration(duration=20)
f = calendar.filter('owner', search_name='e')
# print(len(filter_a))
pprint(f)
# pprint(calendar.events)
