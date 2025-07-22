def sort_months_by_days(months_dict):
    """Sorts a dictionary of months and their days by the number of days.

    Args:
        months_dict: A dictionary where keys are month names (strings) and values
                     are the number of days (integers).

    Returns:
        A new dictionary sorted by the number of days in ascending order.
    """
    sorted_months = dict(sorted(months_dict.items(), key=lambda item: item[1]))
    return sorted_months

# Example usage:
months = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}

sorted_months = sort_months_by_days(months)
print(sorted_months)