def convert_volume(value, unit_from, unit_to):
    try:
        value = float(value)

        conversion_factors = {
            'Liters': 1,
            'Gallons': 0.264172,
            'Quarts': 1.05669,
            'Cubic Meters': 0.001,
            'Cubic Feet': 0.0353147
        }

        converted_value = value * conversion_factors[unit_to] / conversion_factors[unit_from]
        return converted_value

    except ValueError:
        return "Invalid Input"


# Testing the conversion function
def main():
    # Test cases
    test_cases = [
        (10, 'Liters', 'Gallons'),  # Expected output: 2.64172
        (5, 'Gallons', 'Liters'),   # Expected output: 18.92706
        (100, 'Quarts', 'Liters'),  # Expected output: 94.6353
        (50, 'Cubic Meters', 'Cubic Feet'),  # Expected output: 1765.73
        (15, 'Cubic Feet', 'Cubic Meters')   # Expected output: 0.424768
    ]

    for value, unit_from, unit_to in test_cases:
        converted_value = convert_volume(value, unit_from, unit_to)
        print(f"{value} {unit_from} is equal to {converted_value} {unit_to}")


if __name__ == "__main__":
    main()
