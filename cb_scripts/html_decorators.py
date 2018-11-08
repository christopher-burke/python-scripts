#!/usr/bin/env python3

"""HTML Decorators Example.

Example of HTML decorators.
"""


from functools import wraps


def italic(func):
    @wraps(func)
    def wrapp(*args):
        return f'<em>{func(*args)}</em>'
    return wrapp


def bold(func):
    @wraps(func)
    def wrapp(*args):
        return f'<strong>{func(*args)}</strong>'
    return wrapp


def paragraph(func):
    @wraps(func)
    def wrapp(*args):
        return f'<p>{func(*args)}</p>'
    return wrapp


@paragraph
@bold
@italic
def html(content=None):
    return content if content else ''


@italic
def emphasize(content=None):
    """Emphasize tags."""
    return content if content else ''


@bold
def strong(content=None):
    """Bold tags."""
    return content if content else ''


if __name__ == "__main__":
    # Samples
    # emphasize = italic(lambda x: x)
    print(emphasize("Italic Text"))
    print(emphasize())

    # strong = bold(italic(lambda x: x))
    print(strong("Bold Text"))
    print(strong())

    # Test
    _test = paragraph(bold(italic(lambda x: x)))
    print(_test('this is fine.'))
    print(html('this is fine.'))
    assert html('this is fine.') == _test('this is fine.'), "Error."
    print("Passed")
