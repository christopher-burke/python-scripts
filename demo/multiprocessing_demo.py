#!/usr/bin/env python3

"""multiprocessing demo."""

import os
from multiprocessing import Process, current_process


def square(number: int):
    """
    Square number.

    :return: number²
    """
    result = number * number
    process = current_process()
    print(f'{number}² = {result} '
          f'by process: {process.name} pid: {process.pid}')
    return result


if __name__ == '__main__':
    numbers = range(1, 101)
    processes = []

    for index, number in enumerate(numbers):
        process = Process(target=square, args=(number,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
