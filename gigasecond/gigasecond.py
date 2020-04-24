import datetime

'''
1,000,000,000 seconds = 31 yrs, 258 days, 1 hr, 46 min, 40 sec.
'''
def add(moment):
    gigasecond = datetime.timedelta(days=11574, seconds=6400, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
    return moment + gigasecond