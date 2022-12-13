import datetime

# d = datetime.date(2016, 7, 24)
# tday = datetime.date.today()
# print(tday)
# print(tday.year)
# print(tday.weekday()) # Monday 0 Sunday 6
# print(tday.isoweekday()) # Monday 1 Sunday 7

# tdelta = datetime.timedelta(days=7)
# # print(tday + tdelta)
# print(tday - tdelta)

# date2 = date1 + timedelta 
# timedelta = date1 + date2

# bday = datetime.date(2023, 3, 18)

# till_bday = bday - tday
# # print(till_bday)
# print(till_bday.days)
# print(till_bday.total_seconds())

# t = datetime.time(9, 30, 45, 100000)
# print(t)
# print(t.hour)
# t = datetime.day gives the day, months and year only
# t = datetime.time gives the hour, minutes, seconds and microseconds 
# t = datetime.datetime gives access to everything

# dt = datetime.datetime(2016, 7, 26, 12, 30, 45, 100000)
# print(dt)
# print(dt.date())
# print(dt.time())
# print(dt.year)

# tdelta = datetime.timedelta(days=7)
# print(dt + tdelta)

# dt_today = datetime.datetime.today()
# print(dt_today)

# dt_now = datetime.datetime.now()
# print(dt_now)

# dt_utcnow = datetime.datetime.utcnow()
# print(dt_utcnow)

import pytz 

# dt = datetime.datetime(2016, 7, 26, 12, 30, 45, tzinfo=pytz.UTC)
# print(dt)

# dt_now = datetime.datetime.now(tz=pytz.UTC)
# print(dt_now)

# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow)

# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

# dt_lag = dt_utcnow.astimezone(pytz.timezone('Africa/Lagos'))
# print(dt_lag)

# for tz in pytz.all_timezones:
#     print(tz)

# dt_lag = datetime.datetime.now()
# lag_tz = pytz.timezone('Africa/Lagos')

# dt_lag = lag_tz.localize(dt_lag)

# dt_east = dt_lag.astimezone(pytz.timezone('US/Eastern'))
# print(dt_east)

# dt_lag = datetime.datetime.now()
# print(dt_lag.strftime('%B %d, %Y'))

dt_str = 'December 13, 2022'

dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)

# strftime -> Datetime to String
# strptime -> String to Datetime