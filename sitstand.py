#!/usr/bin/env python3

"""Script to tell me to Sitdown and Standup throughout the day."""


import signal
import sys
import time
from subprocess import Popen, PIPE
from datetime import datetime

import logging
logging.getLogger(name=__name__)
logging.basicConfig(level=logging.DEBUG)
# To disable debug, uncomment out bottom line.
# logging.disable(logging.CRITICAL)


def say(phrase):
    """Say the time and phrase, using the macOS 'say' command."""
    now = datetime.now().strftime("%I:%M %p")
    Popen(f"say \"It's {now}! {phrase}\".", shell=True, stdout=PIPE)
    logging.debug(f"say \"It's {now}! {phrase}\".")


def sitdown(interval=600):
    """Sitdown function.

    On the interval (seconds), use the say function to tell the user
    to "Sitdown".
    Wait the interval, default is 10 mins (600 seconds).
    Lastly  tell the user to Stand back up.
    """
    say("Sitdown")
    time.sleep(interval)  # 10 minute delay (10 * 60)
    say("Stand back up.")


class PeriodicEvent:
    """PeriodicEvent class.

    Handles running our task function over an interval time.
    Threading module used to function on the interval.
    Signal module is used to handle the termination.

    Credit Source:
    * https://www.reddit.com/r/Python/comments/2cgirl/\
    best_way_for_an_everrunning_loop/cjg7n59/

    """

    def __init__(self, interval, func):
        """Set the interval and func of the Periodic Event."""
        self.interval = interval
        self.func = func
        self.terminate = threading.Event()

    def _signals_install(self, func):
        """Install signals to the func.

        SIGINT - Ctrl+C
        SIGTERM - kill <pid>
        """
        for sig in [signal.SIGINT, signal.SIGTERM]:
            signal.signal(sig, func)

    def _signal_handler(self, signum, frame):
        """Handle the signals received from the user."""
        self.terminate.set()

    def run(self):
        """Run the func until terminated by user.

        When the func _signal_handler is called, the PeriodicEvent will
        terminate.
        """
        self._signals_install(self._signal_handler)
        while not self.terminate.is_set():
            self.func()
            self.terminate.wait(self.interval)
        self._signals_install(signal.SIG_DFL)


def main():
    """Tell the user to sit and stand."""
    task = PeriodicEvent(2700, sitdown)  # 45 minutes (45 * 60)
    task.run()
    return 0


if __name__ == "__main__":
    sys.exit(main())
