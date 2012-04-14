import datetime
sundays=0
for year in range(1901,2001,1):
		for month in range(1,13,1):
				if datetime.date(year,month,1).weekday()==0: sundays+=1
print "number of sundays on which 1st of a month falls are",sundays