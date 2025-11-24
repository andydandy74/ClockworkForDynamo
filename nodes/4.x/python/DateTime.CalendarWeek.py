import clr
import datetime
year = IN[0]
month = IN[1]
day = IN[2]
OUT = datetime.date(year, month, day).isocalendar()[1]