#!/usr/bin/env python3

"""Time to go."""

import logging
from datetime import datetime, time
from subprocess import Popen, PIPE
from time import sleep

logging.basicConfig(level=logging.DEBUG)


DEBUG = True
DELAY = 10
TIME_TO_LEAVE = time(17,  00)  # '05:00 PM'
TIME_TO_GET_READY = time(16, 30)  # '04:30 PM'


def say(phrase):
    """Say the time and phrase, using the macOS 'say' command."""
    now = datetime.now().strftime("%I:%M %p")
    Popen(f"say \"It's {now}! {phrase}\".", shell=True, stdout=PIPE)
    logging.debug(f"say \"It's {now}! {phrase}\".")


def logic(time_):
    """Logic to say when its time to get ready or to go."""
    phrase = (False, '',)
    if time_ >= TIME_TO_LEAVE:
        phrase = (True, "Time to go home.",)

    if time_ >= TIME_TO_GET_READY and time_ < TIME_TO_LEAVE:
        phrase = (True, "Time to start packing up to go home.")

    return phrase


def go_time():
    """Say the time to get ready or time to go."""
    while True:
        time_now = datetime.now().time()
        phrase = logic(time_now)
        speak, phrase_ = phrase
        if speak:
            say(phrase_)
        sleep(DELAY)


if __name__ == "__main__":
    go_time()
