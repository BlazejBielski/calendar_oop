import datetime

from data_generator import DataGenerator

event_data = DataGenerator(
    datetime.date.today() + datetime.timedelta(days=10),
    (15, 180),
    ['lunch', 'ceo meeting', 'lecture', 'seminar', 'sport event'],
    ['nice meeting', 'troublesome meeting', 'god, I hate that', 'kill me', 'emergency meeting'],
    ['Pawel', 'Marek', 'Darek', 'Jarek', 'Andrzej', 'Ryszard'],
    False,
    False,
)

event_datas = event_data.generate_data(150)
event_data.save_data(event_datas, 'event_data.json')

reminder_data = DataGenerator(
    datetime.date.today() + datetime.timedelta(days=10),
    (15, 180),
    ['lunch', 'ceo meeting', 'lecture', 'seminar', 'sport event'],
    ['nice meeting', 'troublesome meeting', 'god, I hate that', 'kill me', 'emergency meeting'],
    ['Pawel', 'Marek', 'Darek', 'Jarek', 'Andrzej', 'Ryszard'],
    True,
    False,
)

reminders = reminder_data.generate_data(50)
reminder_data.save_data(reminders, 'remind_data.json')

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
