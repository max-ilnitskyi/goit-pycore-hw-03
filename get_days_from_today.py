from datetime import datetime


def get_days_from_today(date):
    try:
        dateObj = datetime.strptime(date, "%Y-%m-%d")
    except Exception:
        print("Wrong format")
        return

    delta = datetime.today() - dateObj

    return delta.days
