#!/usr/bin/env python3

"""Account Expiration

Calcuate the value in Active Directory accountExpires attribute.

According to Microsoft

https://msdn.microsoft.com/en-us/library/ms675098(v=vs.85).aspx

# Account-Expires attribute #
The date when the account expires.
This value represents the number of 100-nanosecond intervals since January 1, 1601 (UTC).
A value of 0 or 0x7FFFFFFFFFFFFFFF (9223372036854775807) indicates that the account never expires.

"""

from datetime import datetime as dt
import math


ACCOUNT_EXPIRATION_DATE = dt(1601, 1, 1, 0, 0, 0)
now = dt.now()


def calculate_nanoseconds(from_, to_):
    delta = to_ - from_
    return delta.total_seconds() / 0.0000001


def main():
    now = dt.now()
    value = calculate_nanoseconds(from_=ACCOUNT_EXPIRATION_DATE, to_=now)
    value = math.floor(value)
    print(f'{value:f}'.split('.')[0])


if __name__ == "__main__":
    main()
