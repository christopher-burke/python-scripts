#!/usr/bin/env python3


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/', methods=['POST'])
def index():
    """Index method."""
    return None


if __name__ == "__main__":
    app.run()
