import calendar
import datetime

today = datetime.datetime.today()
now_calendar = calendar.TextCalendar()
now_calendar.prmonth(today.year, today.month)
