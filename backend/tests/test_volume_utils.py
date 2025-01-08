import pytest
from backend.app.volume_utils import VolumeConverter

def test_convert_litre_to_us_gallon():
    assert pytest.approx(VolumeConverter.convert(1, "litre", "us_gallon")) == 0.264172
    assert pytest.approx(VolumeConverter.convert(10, "litre", "us_gallon")) == 2.64172

def test_convert_us_gallon_to_litre():
    assert pytest.approx(VolumeConverter.convert(1, "us_gallon", "litre")) == 3.78541
    assert pytest.approx(VolumeConverter.convert(2, "us_gallon", "litre")) == 7.57082

def test_convert_cubic_m_to_cubic_cm():
    assert pytest.approx(VolumeConverter.convert(1, "cubic_m", "cubic_cm")) == 1_000_000
    assert pytest.approx(VolumeConverter.convert(0.5, "cubic_m", "cubic_cm")) == 500_000

def test_convert_cubic_cm_to_cubic_m():
    assert pytest.approx(VolumeConverter.convert(1_000_000, "cubic_cm", "cubic_m")) == 1
    assert pytest.approx(VolumeConverter.convert(500_000, "cubic_cm", "cubic_m")) == 0.5

def test_convert_us_fluid_ounce_to_us_cup():
    assert pytest.approx(VolumeConverter.convert(8, "us_fluid_ounce", "us_cup")) == 1
    assert pytest.approx(VolumeConverter.convert(16, "us_fluid_ounce", "us_cup")) == 2

def test_convert_us_cup_to_us_fluid_ounce():
    assert pytest.approx(VolumeConverter.convert(1, "us_cup", "us_fluid_ounce")) == 8
    assert pytest.approx(VolumeConverter.convert(2, "us_cup", "us_fluid_ounce")) == 16

def test_convert_cubic_mile_to_cubic_yard():
    assert pytest.approx(VolumeConverter.convert(1, "cubic_mile", "cubic_yard")) == 5_451_776_000
    assert pytest.approx(VolumeConverter.convert(0.5, "cubic_mile", "cubic_yard")) == 2_725_888_000

def test_convert_cubic_yard_to_cubic_mile():
    assert pytest.approx(VolumeConverter.convert(5_451_776_000, "cubic_yard", "cubic_mile")) == 1
    assert pytest.approx(VolumeConverter.convert(2_725_888_000, "cubic_yard", "cubic_mile")) == 0.5

def test_invalid_conversion():
    with pytest.raises(ValueError, match="Unsupported unit"):
        VolumeConverter.convert(100, "invalid_unit", "cubic_m")
    with pytest.raises(ValueError, match="Unsupported unit"):
        VolumeConverter.convert(100, "cubic_m", "invalid_unit")
