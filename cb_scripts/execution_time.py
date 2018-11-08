#!/usr/bin/env python3

"""
Execution Time.

Time the execution of code in python.

Uses `time` module.
"""


import time


class ExecutionTime:
    """Execution Time.

    Timer for measuring code execution time.
    """

    def __init__(self):
        """Create ExecutionTime object and set the start_time."""
        self.start_time = time.time()

    def restart(self):
        """Reset the start time."""
        self.start_time = time.time()

    def duration(self):
        """Return time delta from current time to start_time."""
        return time.time() - self.start_time

    def __repr__(self):
        """Return Class __repr__ string."""
        return f'{__class__.__name__}()'
