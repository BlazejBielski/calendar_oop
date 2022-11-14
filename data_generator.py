import json
import random
import datetime


class DataGenerator:

    def __init__(self, beginning_date, duration_range, titles, descriptions, users, reminder=False, workshop=False):
        self.beginning_date = beginning_date
        self.duration_range = duration_range
        self.titles = titles
        self.descriptions = descriptions
        self.users = users
        self.reminder = reminder
        self.workshop = workshop

    def generate_data(self, amount):
        events = []

        for idx in range(amount):
            event = {
                'idx': idx,
                'start_date': f'{(self.beginning_date + datetime.timedelta(hours=random.randint(1, 5000))):%Y/%m/%d %H:%M}',
                'duration': random.randint(*self.duration_range),
                'title': random.choice(self.titles),
                'description': random.choice(self.descriptions),
                'owner': random.choice(self.users),
            }

            if self.reminder:
                events['reminder'] = random.choice([True, False])

            if self.workshop:
                events['workshop'] = random.choices(self.users, k=random.randint(3, 20))

            events.append(event)

        return events

    @staticmethod
    def save_data(data, path):
        with open(path, 'w') as file:
            json.dump(data, file)


event_data = DataGenerator(
    datetime.date.today() + datetime.timedelta(days=10),
    (15, 180),
    ['lunch', 'ceo meeting', 'lecture', 'seminar', 'sport event'],
    ['nice meeting', 'troublesome meeting', 'god, I hate that', 'kill me', 'emergency meeting'],
    ['Pawel', 'Marek', 'Darek', 'Jarek', 'Andrzej', 'Ryszard'],
    False,
    False,
)

events = event_data.generate_data(150)
event_data.save_data(events, 'event_data.json' )

remind_data = DataGenerator(
    datetime.date.today() + datetime.timedelta(days=10),
    (15, 180),
    ['lunch', 'ceo meeting', 'lecture', 'seminar', 'sport event'],
    ['nice meeting', 'troublesome meeting', 'god, I hate that', 'kill me', 'emergency meeting'],
    ['Pawel', 'Marek', 'Darek', 'Jarek', 'Andrzej', 'Ryszard'],
    True,
    False,
)

reminders = remind_data.generate_data(50)
remind_data.save_data(reminders, 'remind_data.json')

workshop_data = DataGenerator(
    datetime.date.today() + datetime.timedelta(days=10),
    (15, 180),
    ['lunch', 'ceo meeting', 'lecture', 'seminar', 'sport event'],
    ['nice meeting', 'troublesome meeting', 'god, I hate that', 'kill me', 'emergency meeting'],
    ['Pawel', 'Marek', 'Darek', 'Jarek', 'Andrzej', 'Ryszard'],
    False,
    True,
)

workshops = workshop_data.generate_data(50)
workshop_data.save_data(workshops, 'workshop_data.json')
