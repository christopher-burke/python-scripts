#!/usr/bin/env python3

"""Markdown list maker.

A useful tool to make quick Markdown lists out of text.
"""


from textwrap import dedent, indent


def md_list(text):
    """Return a string of Markdown list items.

    This function uses dedent and indent from textwrap.

    The input text is first run through dedent. The from
    dedent are then called with the string.strip() function,
    this removes all white space. Finally the text is
    used in the indent function with the prefix of "* " argument.
    """
    return indent(dedent(text).strip(), prefix="* ")


if __name__ == "__main__":
    sample = """
    list item 1
    list item 2
    list item 3
    """

    print(md_list(sample))
