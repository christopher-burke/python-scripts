from flask import Flask, render_template
from drum import bingo_drum

app = Flask(__name__)

# Global Setup for game.
called = []
bingo_balls = []


def caller():
    drum = bingo_drum()
    for ball in drum:
        yield ball
        global called
        called.append(ball)


called = []
bingo_balls = []
bingo_caller = caller()


# Routes
@app.route('/')
def hello():
    return "Hello World!"


@app.route('/reset')
def reset():
    global called
    global bingo_balls
    global bingo_caller
    called = []
    bingo_balls = []
    bingo_caller = caller()
    return "Bingo Caller Reset."


@app.route('/game')
def game():
    global called
    try:
        ball = next(bingo_caller)
    except StopIteration:
        ball = called[-1]
    if called:
        called_css_ids = ",".join([f'#{ball}' for ball in called])
    else:
        called_css_ids = 'None'
    return render_template(
                            'board.html',
                            ball=ball,
                            called=called,
                            called_css_ids=called_css_ids
                          )


@app.route('/view')
def view():
    global called
    if called:
        called_css_ids = ",".join([f'#{ball}' for ball in called])
        ball = called[-1]
    else:
        called_css_ids = 'None'
    return render_template('board.html',
                            ball=ball,
                            called=called,
                            called_css_ids=called_css_ids)


if __name__ == '__main__':
    app.run()
