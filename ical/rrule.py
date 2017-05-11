# BEGIN:VEVENT
# DTSTART;TZID=Asia/Tokyo:20170409T080000
# DTEND;TZID=Asia/Tokyo:20170409T100000
# RRULE:FREQ=WEEKLY;UNTIL=20180324T230000Z;BYDAY=SU
# DESCRIPTION:
# LOCATION:
# SUMMARY:
# END:VEVENT

from datetime import datetime
from icalendar import Calendar, Event, vRecur
import pytz


def display(cal):
    return cal.to_ical().replace(b'\r\n', b'\n').decode()


tz = pytz.timezone('Asia/Tokyo')

cal = Calendar()
cal.add('attendee', 'MAILTO:' + 'foo@example.com')
e = Event()
e.add('dtstart', datetime(2017, 4, 1, 11, 00, tzinfo=tz))
e.add('dtend', datetime(2017, 4, 1, 16, 00, tzinfo=tz))
rec = vRecur()
rec['FREQ'] = 'WEEKLY'
rec['BYDAY'] = 'MO'
rec['UNTIL'] = datetime(2018, 3, 31)
e.add('RRULE', rec)
cal.add_component(e)
print(display(cal))
