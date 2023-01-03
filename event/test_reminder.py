from datetime import datetime, timedelta

import pytest

from event import Reminder


@pytest.fixture()
def reminder():
    return Reminder(1, datetime.now() + timedelta(days=1), 30, '', '', '', True)


def test_duration_less_than_ten_minutes_rise_error():
    with pytest.raises(ValueError) as excinfo:
        r = Reminder(1, datetime.now() + timedelta(days=1), 5, '', '', '', True)

        assert 'Wrong data type' in str(excinfo.value)


def test_duration_change_to_less_than_ten_minutes_raise_value_error(reminder):
    with pytest.raises(ValueError) as excinfo:
        reminder.duration = 5

        assert 'can not be shorter than 10 minutes' in str(excinfo.value)


def test_duration_positive(reminder):
    assert reminder.duration == 30



