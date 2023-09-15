from temperature_converter import celsius_to_fahrenheit

def test_celsius_to_fahrenheit():
    # Test freezing point of water in Celsius (0°C)
    assert celsius_to_fahrenheit(0) == 32

    # Test boiling point of water in Celsius (100°C)
    assert celsius_to_fahrenheit(100) == 212

    # Test a random temperature in Celsius (25°C)
    assert celsius_to_fahrenheit(25) == 77
