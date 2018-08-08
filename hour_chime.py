#!/usr/bin/env python3


"""Play sound file at the top of every hour.

    Full path to sound file

    Requires:
    shell from dev_utils.
    schedule package : https://github.com/dbader/schedule

"""


import sys
import schedule
import time
from dev_utils import shell
from functools import partial


def alert(sound):
    """Alert sound played via shell.

    Using shell from dev_tools, play the sound path file
    with the afplay command (macOS).
    """
    return shell(f'afplay {sound}')


if __name__ == "__main__":
    sound_file = sys.argv[1]
    job = partial(alert, sound_file)
    schedule.every().hour.at("00:00").do(job_func=job)

    while True:
        schedule.run_pending()
        time.sleep(1)
