from datetime import datetime, timedelta, date


def get_upcoming_birthdays(users):
    current_date = date.today()
    users_to_congratulate = []
  

    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = date(
            current_date.year, birthday_date.month, birthday_date.day
        )
        birthday_next_year = date(
            current_date.year + 1, birthday_date.month, birthday_date.day
        )

        next_birthday = (
            birthday_next_year
            if birthday_this_year < current_date
            else birthday_this_year
        )

        days_to_birthday = (next_birthday - current_date).days

        if days_to_birthday > 7:
            continue

        days_from_birthday_to_congratulation_date = (
            0 if next_birthday.weekday() < 5 else (6 - next_birthday.weekday()) + 1
        )

        congratulation_date = (
            next_birthday + timedelta(days=days_from_birthday_to_congratulation_date)
            if days_from_birthday_to_congratulation_date
            else next_birthday
        )
        
        print(congratulation_date)

        users_to_congratulate.append(
            {
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            }
        )

    return users_to_congratulate
