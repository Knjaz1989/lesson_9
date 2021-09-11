import calendar
import requests
import datetime


def get_date():
    year, month, day = str(datetime.date.today()).split('-')
    if not int(day) < 3:
        day = str("{:02d}".format(int(day) - 2))
    else:
        if not int(month) == 1:
            month = str("{:02d}".format(int(month) - 1))
            day = str("{:02d}".format(calendar.monthrange(int(year), int(month))[1] + int(day) - 2))
        else:
            year = str(int(year) - 1)
            month = '12'
            day = str("{:02d}".format(calendar.monthrange(int(year), int(month))[1] + int(day) - 2))
    return '-'.join([year, month, day])


def get_questions(date=get_date()):
    response = requests.get("http://api.stackexchange.com/2.3/search/advanced",
                            headers={'Accept': 'application/json'},
                            params={"tagged": 'Python', "fromdate": date, "order": "desc",
                                    "site": "stackoverflow", "sort": "activity"})
    for i in [item["title"] for item in response.json()["items"]]:
        print(i)


get_questions()
