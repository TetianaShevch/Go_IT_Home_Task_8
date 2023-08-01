from datetime import datetime, date
from main import get_birthdays_per_week

workmates = [
    {"John": "1985-08-03"},
    {"Emily": "1992-07-31"},
    {"Michael": "1978-08-04"},
    {"Sarah": "1990-07-30"},
    {"David": "1987-09-30"},
    {"Jessica": "1983-02-28"},
    {"Daniel": "1995-08-03"},
    {"Jennifer": "1989-04-06"},
    {"Christopher": "1980-12-24"},
    {"Elizabeth": "1998-08-05"},
    {"Matthew": "1984-08-06"},
    {"Olivia": "1993-10-14"},
]
    
if __name__ == "__main__":
    get_birthdays_per_week(workmates)
