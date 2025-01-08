import pytest
from backend.app.time_utils import TimeConverter

def test_convert_second_to_millisecond():
    assert pytest.approx(TimeConverter.convert(1, "second", "millisecond")) == 1000
    assert pytest.approx(TimeConverter.convert(2, "second", "millisecond")) == 2000

def test_convert_millisecond_to_second():
    assert pytest.approx(TimeConverter.convert(1000, "millisecond", "second")) == 1
    assert pytest.approx(TimeConverter.convert(2000, "millisecond", "second")) == 2

def test_convert_hour_to_minute():
    assert pytest.approx(TimeConverter.convert(1, "hour", "minute")) == 60
    assert pytest.approx(TimeConverter.convert(2, "hour", "minute")) == 120

def test_convert_minute_to_hour():
    assert pytest.approx(TimeConverter.convert(60, "minute", "hour")) == 1
    assert pytest.approx(TimeConverter.convert(120, "minute", "hour")) == 2

def test_convert_day_to_hour():
    assert pytest.approx(TimeConverter.convert(1, "day", "hour")) == 24
    assert pytest.approx(TimeConverter.convert(2, "day", "hour")) == 48

def test_convert_hour_to_day():
    assert pytest.approx(TimeConverter.convert(24, "hour", "day")) == 1
    assert pytest.approx(TimeConverter.convert(48, "hour", "day")) == 2

def test_convert_week_to_day():
    assert pytest.approx(TimeConverter.convert(1, "week", "day")) == 7
    assert pytest.approx(TimeConverter.convert(2, "week", "day")) == 14

def test_convert_day_to_week():
    assert pytest.approx(TimeConverter.convert(7, "day", "week")) == 1
    assert pytest.approx(TimeConverter.convert(14, "day", "week")) == 2

def test_convert_year_to_month():
    assert pytest.approx(TimeConverter.convert(1, "year", "month")) == 12
    assert pytest.approx(TimeConverter.convert(2, "year", "month")) == 24

def test_convert_month_to_year():
    assert pytest.approx(TimeConverter.convert(12, "month", "year")) == 1
    assert pytest.approx(TimeConverter.convert(24, "month", "year")) == 2

def test_invalid_conversion():
    with pytest.raises(ValueError, match="Unsupported unit"):
        TimeConverter.convert(100, "invalid_unit", "second")
    with pytest.raises(ValueError, match="Unsupported unit"):
        TimeConverter.convert(100, "second", "invalid_unit")
