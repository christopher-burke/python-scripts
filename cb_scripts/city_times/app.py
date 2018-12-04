#!/usr/bin/env python3


from flask import Flask, render_template, request
from collections import namedtuple

app = Flask(__name__)


CityTime = namedtuple('CityTime', ['name', 'time'])


@app.route('/')
@app.route('/', methods=['POST'])
def index():
    """Index method."""
    data = []
    if request.method == 'POST':
        city_a = request.form.get('city-a')
        city_b = request.form.get('city-b')

        for city in (city_a, city_b,):
            time = 1  # TODO: Add function to look up time.
            data.append(CityTime(name=city, time=time))

    return render_template("time.html", data=data)


if __name__ == "__main__":
    app.run()
