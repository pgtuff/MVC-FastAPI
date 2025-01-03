def mm_to_m(value):
    return value / 1000

def cm_to_m(value):
    return value / 100

def m_to_m(value):
    return value

def km_to_m(value):
    return value * 1000

def micrometer_to_m(value):
    return value / 1e6

def nanometer_to_m(value):
    return value / 1e9

def yard_to_m(value):
    return value * 0.9144

def foot_to_m(value):
    return value * 0.3048

def mile_to_m(value):
    return value * 1609.34

def inch_to_m(value):
    return value * 0.0254

def light_year_to_m(value):
    return value * 9.461e15

def m_to_mm(value):
    return value * 1000

def m_to_cm(value):
    return value * 100

def m_to_km(value):
    return value / 1000

def m_to_micrometer(value):
    return value * 1e6

def m_to_nanometer(value):
    return value * 1e9

def m_to_yard(value):
    return value / 0.9144

def m_to_foot(value):
    return value / 0.3048

def m_to_mile(value):
    return value / 1609.34

def m_to_inch(value):
    return value / 0.0254

def m_to_light_year(value):
    return value / 9.461e15

def convert_length(value, from_unit, to_unit):
    # Mapping units to conversion functions to/from meters
    to_meters = {
        "mm": mm_to_m,
        "cm": cm_to_m,
        "m": m_to_m,
        "km": km_to_m,
        "micrometer": micrometer_to_m,
        "nanometer": nanometer_to_m,
        "yard": yard_to_m,
        "foot": foot_to_m,
        "mile": mile_to_m,
        "inch": inch_to_m,
        "light_year": light_year_to_m,
    }

    from_meters = {
        "mm": m_to_mm,
        "cm": m_to_cm,
        "m": m_to_m,
        "km": m_to_km,
        "micrometer": m_to_micrometer,
        "nanometer": m_to_nanometer,
        "yard": m_to_yard,
        "foot": m_to_foot,
        "mile": m_to_mile,
        "inch": m_to_inch,
        "light_year": m_to_light_year,
    }

    if from_unit not in to_meters or to_unit not in from_meters:
        raise ValueError("Unsupported unit. Supported units are: " + ", ".join(to_meters.keys()))

    # Convert from the source unit to meters
    value_in_meters = to_meters[from_unit](value)

    # Convert from meters to the target unit
    return from_meters[to_unit](value_in_meters)