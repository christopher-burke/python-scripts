#!/usr/bin/env python3


""" Site Checker.

Site Checker with Time Scheduling – An application that attempts to
connect to a website or server every so many minutes or a given
time and check if it is up.

If it is down, it will notify you by email or by posting a
notice on screen.

"""

# Third Part Packages
try:
    import requests
except ImportError:
    print('Request package is required. Install requests with pip: `pip install requests`.')

try:
    import schedule
except ImportError:
    print('Schedule package is required. Install schedule with pip: `pip install schedule`.')


import sys
import time


class MessageOutput:
    terminal_messages = {
        True: '{} is up.',
        False: '{} is down. Check internet connection first.',
    }

    def _output(self, url, status):
        raise NotImplementedError

    def alert():
        raise NotImplementedError

    def terminal_output(self, url, status):
        """Output message for the user."""
        print(self.terminal_messages[status(url)].format(url))
        return self.terminal_messages[status(url)].format(url)


class SiteChecker:

    @staticmethod
    def check(url):
        """Check the url, return status of site.

        True - Site is up. OK response.
        False - Site is down.
        """
        r = requests.get(url)
        return r.status_code == requests.codes.ok

    @staticmethod
    def check_test(url):
        """Test function for check. Returns Random True/False."""
        from random import choice
        c = choice([True, False])
        print(f'{c}')
        return c


def scheduler(url,seconds, test=False):
    """Using `schedule` run checker on an interval.

    Run forever, until KeyboardInterrupt or Process Termination.
    """
    mo = MessageOutput()
    sc = SiteChecker()
    status = sc.check
    if test:
        status = sc.check_test
    else:
        status = sc.check
    schedule.every(seconds).seconds.do(job_func=mo.terminal_output,
                                       url=url,
                                       status=sc.check)
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        seconds = sys.argv[2]
        if seconds:
            scheduler(url=url, seconds=int(seconds))
    except (IndexError, ValueError) as e:
        print(e)
        print(f'python ./{__file__}.py <url> <interval in seconds>')
