def swap_units(unit1, unit2):
    """
    Swap two unit values and return the swapped result.

    :param unit1: The first unit
    :param unit2: The second unit
    :return: A tuple with the swapped units
    """
    return unit2, unit1


# Test cases for the swap_units function
def test_swap_units():
    # Define test cases
    test_cases = [
        ("Liters", "Gallons"),
        ("Quarts", "Cubic Meters"),
        ("Cubic Feet", "Liters"),
        ("Gallons", "Quarts")
    ]

    # Run tests
    for unit1, unit2 in test_cases:
        swapped_unit1, swapped_unit2 = swap_units(unit1, unit2)
        print(f"Original: ({unit1}, {unit2}) -> Swapped: ({swapped_unit1}, {swapped_unit2})")


if __name__ == "__main__":
    test_swap_units()
