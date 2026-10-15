def convert_units(value, from_unit, to_unit):
    """
    Convert a value from one unit to another.

    Parameters:
    value (float): The numerical value to convert.
    from_unit (str): The unit of the input value.
    to_unit (str): The unit to convert the value to.

    Returns:
    float: The converted value in the desired unit.
    """
    # Define conversion factors for supported units
    conversion_factors = {
        'meters': 1.0,
        'kilometers': 0.001,
        'centimeters': 100.0,
        'millimeters': 1000.0,
        'inches': 39.3701,
        'feet': 3.28084,
        'yards': 1.09361,
        'miles': 0.000621371
    }

    # Check if the units are supported
    if from_unit not in conversion_factors or to_unit not in conversion_factors:
        raise ValueError("Unsupported unit provided.")

    # Convert the value to meters first
    value_in_meters = value / conversion_factors[from_unit]

    # Convert from meters to the target unit
    converted_value = value_in_meters * conversion_factors[to_unit]

    return converted_value