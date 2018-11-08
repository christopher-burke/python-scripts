#!/usr/bin/env python3


"""Site Checker.

Site Checker with Time Scheduling – An application that attempts to
connect to a website or server every so many minutes or a given
time and check if it is up.

If it is down, it will notify you by email or by posting a
notice on screen.

"""

# Third Part Packages

import sys
import time


def import_error(package):
    """Import error message."""
    return f'{package.capitalize()} package is required.' +\
        f' Install {package} with pip:' + \
        f' `pip install {package}`.'


try:
    import requests
except ImportError:
    print(import_error('request'))


try:
    import schedule
except ImportError:
    print(import_error('schedule'))


class MessageOutput:
    terminal_messages = {
        True: '{} is up.',
        False: '{} is down. Check internet connection first.',
    }

    def _output(self, url, status):
        raise NotImplementedError

    def alert():
        """Alert method."""
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


def scheduler(url, seconds, test=False):
    """Run checker on a schedule.

    Using `schedule` run checker on an interval.

    Run forever, until KeyboardInterrupt or Process Termination.
    """
    mo = MessageOutput()
    sc = SiteChecker()
    status = sc.check
    if test:
        status = sc.check_test
    schedule.every(seconds).seconds.do(job_func=mo.terminal_output,
                                       url=url,
                                       status=status)
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
