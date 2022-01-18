>>> from datetime import date
>>> now = date.today()
>>> now
datetime.date(2022, 1, 18)
>>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
'01-18-22. 18 Jan 2022 is a Tuesday on the 18 day of January.'
>>> now.strftime("%m-%d-%y. %d %m %Y is a %A on the %d day of %B.")
'01-18-22. 18 01 2022 is a Tuesday on the 18 day of January.'
>>> birthday = date(1964, 7, 31)
>>> age = now - birthday
>>> age.days
20990
>>> birthday = date(1996, 9, 24)
>>> age = now - birthday
>>> age.days
9247