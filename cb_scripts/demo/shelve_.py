#!/usr/bin/env python3

"""Shelve demo."""

import shelve

db = shelve.open('devices.db')

print(list(db.keys()))

if '1' not in db:
    db['1'] = 'Raspberry-Pi'
if '2' not in db:
    db['2'] = 'Raspberry-Pi-Zero'
if '3' not in db:
    db['3'] = 'Laptop'

print(list(db.keys()))
print(list(db.values()))

db.close()
