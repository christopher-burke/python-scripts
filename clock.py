#!/usr/bin/env python3


"""Simple clock using tkinter."""


import tkinter
from time import strftime, sleep
import gc

font = 'Source Code Pro'

if __name__ == "__main__":
    ck = tkinter.Label()
    ck['text'] = strftime('%H:%M:%S')
    ck['font'] = f'"{font}" 120 bold'
    ck.pack()

    while True:
        current_time = strftime('%H:%M:%S')
        ck['text'] = current_time
        ck.update()
        sleep(0.0001)
        gc.collect()
