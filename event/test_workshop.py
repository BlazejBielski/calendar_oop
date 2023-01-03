from datetime import datetime, timedelta

import pytest

from event import Workshop


def test_duration_less_than_ten_minutes_rise_error():
    with pytest.raises(ValueError) as excinfo:
        r = Workshop(1, datetime.now() + timedelta(days=1), 5, '', '', '', '')

        assert 'Wrong data type' in str(excinfo.value)
