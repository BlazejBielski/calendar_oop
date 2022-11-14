from pprint import pprint
from datetime import datetime

from data_generator import DataGenerator
from event import Event

events = DataGenerator.load_data('event_data.json')
events_obj = []

for event in events:
    event['start_date'] = datetime.strptime(event['start_date'], '%Y/%m/%d %H:%M')
    events_obj.append(Event(**event))


pprint(events_obj)
