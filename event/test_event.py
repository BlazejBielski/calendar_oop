from datetime import datetime, timedelta

from event import Event
import pytest


@pytest.fixture()
def event():
    return Event(1, datetime.now() + timedelta(days=1), 30, '', '', '')


def test_duration_less_than_ten_minutes_rise_error():
    with pytest.raises(ValueError) as excinfo:
        e = Event(1, datetime.now() + timedelta(days=1), 5, '', '', '')

        assert 'can not be shorter than 10 minutes' in str(excinfo.value)


def test_duration_change_to_less_than_ten_minutes_raise_value_error(event):
    with pytest.raises(ValueError) as excinfo:
        event.duration = 5

        assert 'can not be shorter than 10 minutes' in str(excinfo.value)


def test_duration_positive(event):
    assert event.duration == 30


def test_duration_invalid_type_should_raise_type_error():
    with pytest.raises(TypeError) as excinfo:
        e = Event(1, datetime.now() + timedelta(days=1), '5', '', '', '')

        assert 'Duration should be a positive digit' in str(excinfo.value)


def test_start_date_with_less_than_hour_raise_value_error():
    with pytest.raises(ValueError) as excinfo:
        e = Event(1, datetime.now() + timedelta(hours=0.5), 30, '', '', '')

        assert 'should be not start less than an hour' in str(excinfo.value)


def test_start_date_change_with_less_than_hour_raise_value_error(event):
    with pytest.raises(ValueError) as excinfo:
        event.start_date = datetime.now() + timedelta(hours=0.5)

        assert 'should be not start less than an hour' in str(excinfo.value)


def test_start_date_invalid_value_raises_value_error():
    with pytest.raises(TypeError) as excinfo:
        e = Event(1, 5, 30, '', '', '')

        assert 'Provided value is not date or time' in str(excinfo.value)


def test_start_date_positive(event):
    assert f'{event.start_date:%A %b %y, %H:%M}' == f'{(datetime.now() + timedelta(days=1)):%A %b %y, %H:%M}'
