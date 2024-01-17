"""
This module contains the function get_birthdays_per_week to calculate birthdays
of users for the upcoming week.
"""

from datetime import date, datetime


def get_birthdays_per_week(users):
    """
    Calculates the birthdays of users for the upcoming week.

    Parameters:
    users (list): A list of users, where each user is a dictionary with 'name'
    and 'birthday' keys.

    Returns:
    dict: A dictionary where keys are days of the week, and values are lists
    of names of users whose birthday are on that day of the week.
    """

    if not users:
        return {}

    today = date.today()

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    birthdays = {day: [] for day in weekdays}

    for user in users:
        birthday_this_year = user['birthday'].replace(year=today.year)
        birthday_next_year = user['birthday'].replace(year=today.year + 1)

        # Is the birthday this week or next
        birthday = None
        if birthday_this_year >= today:
            if (birthday_this_year - today).days <= 7:
                birthday = birthday_this_year

        # Birthdays that have already passed this year, but will be next week
        elif (birthday_next_year - today).days <= 7:
            birthday = birthday_next_year

        if birthday:
            day_of_week = birthday.weekday()
            # If it is a weekend, move it to Monday
            if day_of_week >= 5:
                day_of_week = 0

            day_name = weekdays[day_of_week]

            # If the birthday meets the criteria, add it to the dictionary
            if birthday >= today:
                birthdays[day_name].append(user['name'])

    # Remove days that do not have names
    birthdays_dict = {}
    for day_of_week, names_list in birthdays.items():
        if names_list:
            birthdays_dict[day_of_week] = names_list

    birthdays = birthdays_dict

    return birthdays


if __name__ == "__main__":
    users_eg = [
        {"name": "Jan Koum", "birthday": datetime(1976, 12, 7).date()},
        {"name": "Bill Gates", "birthday": datetime(1955, 12, 5).date()}]

    result = get_birthdays_per_week(users_eg)
    print(result)
    # Display the result
    for day_week_name, names in result.items():
        print(f"{day_week_name}: {', '.join(names)}")
