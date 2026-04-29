from length_converter import meters_to_kilometers
from weight_converter import grams_to_kilograms
from temperature_converter import celsius_to_fahrenheit
from volume_converter import liters_to_milliliters
from area_converter import square_meters_to_square_kilometers
from speed_converter import mps_to_kph
from time_converter import seconds_to_minutes
from data_converter import bytes_to_kilobytes


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def main():
    print("Length: 5000 meters = ", meters_to_kilometers(5000), "kilometers")
    print("Weight: 10000 grams = ", grams_to_kilograms(10000), "kilograms")
    print("Temperature: 37°C = ", celsius_to_fahrenheit(37), "°F")
    print("Volume: 3 liters = ", liters_to_milliliters(3), "milliliters")
    print("Area: 1000000 square meters = ", square_meters_to_square_kilometers(1000000), "square kilometers")
    print("Speed: 10 m/s = ", mps_to_kph(10), "km/h")
    print("Time: 120 seconds = ", seconds_to_minutes(120), "minutes")
    print("Data: 2048 bytes = ", bytes_to_kilobytes(2048), "kilobytes")

if __name__ == "__main__":
    main()
