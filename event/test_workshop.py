from datetime import datetime, timedelta

import pytest

from event import Workshop


@pytest.fixture()
def workshop():
    return Workshop(1, datetime.now() + timedelta(days=1), 30, '', '', '', True)


def test_duration_less_than_ten_minutes_rise_error():
    with pytest.raises(ValueError) as excinfo:
        r = Workshop(1, datetime.now() + timedelta(days=1), 5, '', '', '', '')

        assert 'Wrong data type' in str(excinfo.value)


def test_start_date_positive(workshop):
    assert f'{workshop.start_date:%A %b %y, %H:%M}' == f'{(datetime.now() + timedelta(days=1)):%A %b %y, %H:%M}'
