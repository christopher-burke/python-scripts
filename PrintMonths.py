#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Print the calendars for last, this, and next month to display on the desktop."""

__author__ = "Christopher James Burke"
__credits__ = ["Christopher James Burke"]
__version__ = "1.0.7"
__maintainer__ = "Christopher James Burke"
__email__ = "christopherjamesburke@gmail.com"
__status__ = "Production" # __status__  one of "Prototype", "Development", or "Production"
__date__ = "2013/09/21 14:06:13"



import calendar, color
from datetime import datetime

class GeekToolCalendar:

    def __init__(self):
        now = datetime.now()
        calendar.setfirstweekday(calendar.SUNDAY)
        self.year = now.year
        self.month = now.month
        self.day = now.day
        self.format_string = str('%s'+'%3s'*6)
        
    def spaces(self, digit):
        if digit == "0":
            return "  "
        else:
            return '%2s' % (digit)

    def color(self, today_string):
        return color.colored(today_string, 'grey', 'on_yellow')

    def return_print_month(self, year,month):
        """Generator for the last, this and next month."""
        pcal = calendar.month
        for mon in range(month-1,month+2):
            if mon == 0:
                yield pcal(year-1,12)
            elif mon == 13:
                yield pcal(year+1,1)
            else:
                yield pcal(year,mon)

    def current_month(self):
        #Print the Month Header form the pmonth object.
        pmonth = calendar.month(self.year, self.month)
        mcal = calendar.monthcalendar
        print pmonth[:str(pmonth).index('\n')+22].upper(),
        #For each list (week) in mcal list.
        for week in mcal(self.year,self.month):
            try:
                #Try to find the current day.
                ind = week.index(self.day)
                week.pop(ind)
                output_date = '%2s'
                date = self.color(output_date % (self.day))
                if ind == 0:
                    insert = '{0}'
                else:
                    insert = ' {0}'
                week.insert(ind, insert.format(date))
                print str(self.format_string % tuple([self.spaces(str(day)) for day in week]))
            except ValueError:
               print self.format_string % tuple([self.spaces(str(day)) for day in week])
        print #Print new line
        
    def print_month(self,yr,mon,multi=True,pass_mon=1,future_mon=1):
        """Print the last, this and next month."""
        #Get the printed month function from calendar class.
        pcal = calendar.month
        #Get the matrix month function from claendar class.
        mcal = calendar.monthcalendar   
        #To get the Correct last and next month when the current month is December or Janurary.
        if multi:
            for test_mon in range(mon-(pass_mon),mon+(future_mon + 1)):
                if test_mon == 0:
                    yr = yr-1
                    test_mon = 12
                elif test_mon == 13:
                    yr = yr+1
                    test_mon = 1
                if self.month == test_mon:
                    self.current_month()
                else:
                    pmonth  = pcal(yr, test_mon)
                    print pmonth.upper()
        else:
            self.current_month()

if __name__ == "__main__":
    #Using the now.month get last, this and next month and print the calendar.
    gtc = GeekToolCalendar()
    gtc.print_month(gtc.year,gtc.month)