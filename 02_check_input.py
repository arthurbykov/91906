def check_input(value, unit_from, unit_to):
    try:
        # Convert the input value to float
        value = float(value)

        # Check if the input value is negative
        if value < 0:
            return False, "Input value cannot be negative"

        # Conversion factors dictionary
        conversion_factors = {
            'Liters': 1,
            'Gallons': 0.264172,
            'Quarts': 1.05669,
            'Cubic Meters': 0.001,
            'Cubic Feet': 0.0353147
        }

        # Check if the selected units are in the conversion factors dictionary
        if unit_from not in conversion_factors or unit_to not in conversion_factors:
            return False, "Selected units not found"

        # No errors, input is valid
        return True, None

    except ValueError:
        # Handle the case where the input value cannot be converted to float
        return False, "Invalid input value"


# Test the function
if __name__ == "__main__":
    # Test input values
    test_values = [
        ('10', 'Liters', 'Gallons'),  # Valid input
        ('-5', 'Liters', 'Gallons'),  # Negative value
        ('10', 'Kilograms', 'Gallons'),  # Invalid units
        ('abc', 'Liters', 'Gallons')  # Non-numeric input
    ]

    for value, unit_from, unit_to in test_values:
        valid, error_msg = check_input(value, unit_from, unit_to)
        print(f"Value: {value}, Unit From: {unit_from}, Unit To: {unit_to}, Valid: {valid}, Error Message: {error_msg}")
