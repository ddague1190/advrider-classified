from datetime import datetime

def convert_date_format(original_str):
    monthToDay = {
        "Jan": 1,
        "Feb": 2,
        "Mar": 3,
        "Apr": 4,
        "May": 5,
        "Jun": 6,
        "Jul": 7,
        "Aug": 8,
        "Sep": 9,
        "Oct": 10,
        "Nov": 11,
        "Dec": 12,
    }
    [M, D, Y] = original_str.replace(",", "").split(" ")
    temp_date = f"{Y}-{monthToDay[M]}-{D}"
    return datetime.strptime(temp_date, "%Y-%m-%d").date()