from datetime import datetime, timedelta

from data_generator import DataGenerator


def test_generate_data_for_event_all_positive():
    d = DataGenerator(0, "2023/04/08 00:00", 17, "lunch", "nice meeting", "Ryszard")
    assert print(d) == {"idx": 0, "start_date": "2023/04/08 00:00", "duration": 17, "title": "lunch", "description": "nice meeting", "owner": "Ryszard"}