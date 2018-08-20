#!/usr/bin/env python3

"""Number of days from/until start/end of the month.

Using third party package Arrow. `pip install arrow`.
"""

import arrow


class CustomArrow(arrow.Arrow):

    def days_from_start_of_month(self):
        start = self.floor('month').date()
        self.start = start
        return (self.date() - start).days

    def days_till_end_of_month(self):
        end = self.ceil('month').date()
        self.end = end
        return (end - self.date()).days


if __name__ == "__main__":

    factory = arrow.ArrowFactory(CustomArrow)
    custom = factory.now()
    custom.days_from_start_of_month()
    custom.days_till_end_of_month()

    print(
        f'{custom.start} <--{custom.days_from_start_of_month()} [[{custom.date()}]] {custom.days_till_end_of_month()}--> {custom.end}')
