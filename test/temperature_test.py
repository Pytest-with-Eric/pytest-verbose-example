from src.temperature_converter import celsius_to_fahrenheit, fahrenheit_to_celsius

def test_celsius_to_fahrenheit():
    # Test freezing point of water in Celsius (0°C)
    assert celsius_to_fahrenheit(0) == 32

    # Test boiling point of water in Celsius (100°C)
    assert celsius_to_fahrenheit(100) == 21 #2

    # Test a random temperature in Celsius (25°C)
    assert celsius_to_fahrenheit(25) == 77

def test_fahrenheit_to_celsius():
    print("Testing fahrenheit to celsius")
    # Test freezing point of water in Fahrenheit (32°F)
    assert fahrenheit_to_celsius(32) == 0

    # Test freezing point of water in Fahrenheit (212°F)
    assert fahrenheit_to_celsius(212) == 100

    # Test freezing point of water in Fahrenheit (77°F)
    assert fahrenheit_to_celsius(77) == 25
